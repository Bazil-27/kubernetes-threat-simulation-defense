from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.units import cm
import tempfile

def generate_pdf(attacks, events, score):
    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
    doc = SimpleDocTemplate(tmp.name, pagesize=A4, leftMargin=2*cm, rightMargin=2*cm)
    styles = getSampleStyleSheet()
    story = []

    # Title
    title_style = ParagraphStyle("title", fontSize=20, fontName="Helvetica-Bold", spaceAfter=6)
    sub_style   = ParagraphStyle("sub",   fontSize=11, fontName="Helvetica",      textColor=colors.grey, spaceAfter=20)

    story.append(Paragraph("Kubernetes Threat Simulation & Defense", title_style))
    story.append(Paragraph("Phase 4 — Security Report", sub_style))

    # Kubescape Score
    story.append(Paragraph("Kubescape Scores", styles["Heading2"]))
    score_data = [
        ["Benchmark",        "Score"],
        ["Overall",          f"{score.overall}/100"],
        ["MITRE ATT&CK",     f"{score.mitre}%"],
        ["NSA K8s Hardening",f"{score.nsa}%"],
    ]
    score_table = Table(score_data, colWidths=[10*cm, 6*cm])
    score_table.setStyle(TableStyle([
        ("BACKGROUND",  (0,0), (-1,0), colors.HexColor("#1a1a2e")),
        ("TEXTCOLOR",   (0,0), (-1,0), colors.white),
        ("FONTNAME",    (0,0), (-1,0), "Helvetica-Bold"),
        ("ROWBACKGROUNDS", (0,1), (-1,-1), [colors.HexColor("#f5f5f5"), colors.white]),
        ("GRID",        (0,0), (-1,-1), 0.5, colors.lightgrey),
        ("FONTSIZE",    (0,0), (-1,-1), 10),
        ("PADDING",     (0,0), (-1,-1), 8),
    ]))
    story.append(score_table)
    story.append(Spacer(1, 0.5*cm))

    # Attacks
    story.append(Paragraph("Attack Simulations", styles["Heading2"]))
    atk_data = [["#", "Attack", "MITRE ID", "Tactic", "Severity"]]
    for a in attacks:
        atk_data.append([str(a.id), a.name, a.mitre_id, a.mitre_tactic, a.severity.upper()])
    atk_table = Table(atk_data, colWidths=[1*cm, 5*cm, 3*cm, 4*cm, 3*cm])
    atk_table.setStyle(TableStyle([
        ("BACKGROUND",  (0,0), (-1,0), colors.HexColor("#e63946")),
        ("TEXTCOLOR",   (0,0), (-1,0), colors.white),
        ("FONTNAME",    (0,0), (-1,0), "Helvetica-Bold"),
        ("ROWBACKGROUNDS", (0,1), (-1,-1), [colors.HexColor("#fff0f0"), colors.white]),
        ("GRID",        (0,0), (-1,-1), 0.5, colors.lightgrey),
        ("FONTSIZE",    (0,0), (-1,-1), 9),
        ("PADDING",     (0,0), (-1,-1), 7),
    ]))
    story.append(atk_table)
    story.append(Spacer(1, 0.5*cm))

    # Defense Events
    story.append(Paragraph("Defense Events", styles["Heading2"]))
    def_data = [["#", "Tool", "Event", "Blocked"]]
    for e in events:
        def_data.append([str(e.id), e.tool, e.event, "YES" if e.blocked else "DETECTED"])
    def_table = Table(def_data, colWidths=[1*cm, 4*cm, 9*cm, 2.5*cm])
    def_table.setStyle(TableStyle([
        ("BACKGROUND",  (0,0), (-1,0), colors.HexColor("#2d6a4f")),
        ("TEXTCOLOR",   (0,0), (-1,0), colors.white),
        ("FONTNAME",    (0,0), (-1,0), "Helvetica-Bold"),
        ("ROWBACKGROUNDS", (0,1), (-1,-1), [colors.HexColor("#f0fff4"), colors.white]),
        ("GRID",        (0,0), (-1,-1), 0.5, colors.lightgrey),
        ("FONTSIZE",    (0,0), (-1,-1), 9),
        ("PADDING",     (0,0), (-1,-1), 7),
    ]))
    story.append(def_table)

    doc.build(story)
    return tmp.name
