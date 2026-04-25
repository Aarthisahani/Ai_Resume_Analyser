import json
import io
import pdfplumber
from groq import Groq
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from django.http import HttpResponse
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from .models import ResumeResult


@login_required
def index(request):
    return render(request, 'analyser/index.html')


@login_required
def analyse(request):
    if request.method != 'POST':
        return render(request, 'analyser/index.html')

    resume_text = ''
    uploaded_file = request.FILES.get('resume')
    pasted_text = request.POST.get('resume_text', '').strip()
    job_desc = request.POST.get('job_desc', '').strip()
    filename = 'Resume'

    if uploaded_file:
        filename = uploaded_file.name
        try:
            file_bytes = uploaded_file.read()
            with pdfplumber.open(io.BytesIO(file_bytes)) as pdf:
                for page in pdf.pages:
                    text = page.extract_text()
                    if text:
                        resume_text += text + '\n'
            if not resume_text.strip():
                return render(request, 'analyser/index.html',
                              {'error': 'PDF has no readable text! Please paste text instead.'})
        except Exception as e:
            return render(request, 'analyser/index.html',
                          {'error': f'PDF error: {str(e)}'})
    elif pasted_text:
        resume_text = pasted_text
    else:
        return render(request, 'analyser/index.html',
                      {'error': 'Please upload a PDF or paste resume text!'})

    try:
        client = Groq(api_key=settings.GROQ_API_KEY)

        prompt = f"""Analyse this resume and reply ONLY in valid JSON format, no extra text:
{{
  "overall_score": 75,
  "ats_score": 80,
  "skills_found": ["skill1", "skill2"],
  "missing_skills": ["skill1", "skill2"],
  "strengths": ["point1", "point2", "point3"],
  "improvements": ["point1", "point2", "point3"],
  "experience_level": "Junior",
  "suggested_roles": ["role1", "role2", "role3"]
}}

Resume:
{resume_text}

{f'Job Description: {job_desc}' if job_desc else ''}"""

        message = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            max_tokens=1000,
            messages=[{"role": "user", "content": prompt}]
        )

        raw = message.choices[0].message.content
        clean = raw.replace('```json', '').replace('```', '').strip()
        result = json.loads(clean)

        ResumeResult.objects.create(
            user=request.user,
            filename=filename,
            overall_score=result['overall_score'],
            ats_score=result['ats_score'],
            experience_level=result['experience_level'],
            result_json=json.dumps(result)
        )

        return render(request, 'analyser/result.html', {'result': result})

    except Exception as e:
        return render(request, 'analyser/index.html',
                      {'error': f'Error: {str(e)}'})


@login_required
def history(request):
    results = ResumeResult.objects.filter(user=request.user)
    return render(request, 'analyser/history.html', {'results': results})


@login_required
def delete_result(request, pk):
    result = ResumeResult.objects.get(pk=pk, user=request.user)
    result.delete()
    return redirect('/history/')


@login_required
def download_result(request, pk):
    resume = ResumeResult.objects.get(pk=pk, user=request.user)
    result = json.loads(resume.result_json)

    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=A4,
                            rightMargin=40, leftMargin=40,
                            topMargin=40, bottomMargin=40)

    styles = getSampleStyleSheet()
    story = []

    title_style = ParagraphStyle('title', parent=styles['Title'],
                                  fontSize=22, textColor=colors.HexColor('#667eea'),
                                  spaceAfter=6)
    story.append(Paragraph("AI Resume Analysis Report", title_style))
    story.append(Paragraph(f"File: {resume.filename}", styles['Normal']))
    story.append(Paragraph(f"Date: {resume.created_at.strftime('%d %B %Y')}", styles['Normal']))
    story.append(Spacer(1, 15))

    score_data = [
        ['Overall Score', 'ATS Score', 'Experience Level'],
        [f"{result['overall_score']}/100", f"{result['ats_score']}/100", result['experience_level']],
    ]
    score_table = Table(score_data, colWidths=[2.2*inch, 2.2*inch, 2.2*inch])
    score_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#667eea')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('FONTSIZE', (0, 1), (-1, 1), 16),
        ('FONTNAME', (0, 1), (-1, 1), 'Helvetica-Bold'),
        ('BACKGROUND', (0, 1), (-1, 1), colors.HexColor('#f8f7ff')),
        ('BOX', (0, 0), (-1, -1), 1, colors.HexColor('#667eea')),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#cccccc')),
        ('TOPPADDING', (0, 0), (-1, -1), 10),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 10),
    ]))
    story.append(score_table)
    story.append(Spacer(1, 15))

    section_style = ParagraphStyle('section', parent=styles['Heading2'],
                                    fontSize=13, textColor=colors.HexColor('#667eea'),
                                    spaceBefore=10, spaceAfter=6)
    item_style = ParagraphStyle('item', parent=styles['Normal'],
                                 fontSize=11, spaceAfter=3, leftIndent=10)

    story.append(Paragraph("Skills Found", section_style))
    story.append(Paragraph(", ".join(result['skills_found']), item_style))
    story.append(Spacer(1, 8))

    story.append(Paragraph("Missing Skills", section_style))
    story.append(Paragraph(", ".join(result['missing_skills']), item_style))
    story.append(Spacer(1, 8))

    story.append(Paragraph("Strengths", section_style))
    for s in result['strengths']:
        story.append(Paragraph(f"• {s}", item_style))
    story.append(Spacer(1, 8))

    story.append(Paragraph("Areas to Improve", section_style))
    for i in result['improvements']:
        story.append(Paragraph(f"• {i}", item_style))
    story.append(Spacer(1, 8))

    story.append(Paragraph("Suggested Roles", section_style))
    story.append(Paragraph(", ".join(result['suggested_roles']), item_style))

    doc.build(story)
    buffer.seek(0)

    response = HttpResponse(buffer, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="resume_analysis_{resume.pk}.pdf"'
    return response


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'analyser/signup.html', {'form': form})