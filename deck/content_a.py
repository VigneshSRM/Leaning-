# -*- coding: utf-8 -*-
"""Front matter + Modules 01-03."""
from .visuals import roadmap, chain, arch_assistant, pipeline, model_compare


def C(kicker, title, summary, bullets, visual=None, outcome=None, notes=None, **kw):
    d = dict(kind="concept", kicker=kicker, title=title, summary=summary, bullets=bullets,
             visual=visual, outcome=outcome, notes=notes)
    d.update(kw)
    return d


def W(kicker, title, summary, visual, bullets=None, outcome=None, notes=None, **kw):
    d = dict(kind="wide", kicker=kicker, title=title, summary=summary, visual=visual,
             bullets=bullets, outcome=outcome, notes=notes)
    d.update(kw)
    return d


def S(kicker, title, summary, bullets, visual, outcome=None, notes=None, **kw):
    d = dict(kind="split", kicker=kicker, title=title, summary=summary, bullets=bullets,
             visual=visual, outcome=outcome, notes=notes)
    d.update(kw)
    return d


def D(kicker, title, summary, left, right=None, bullets=None, outcome=None, notes=None, **kw):
    d = dict(kind="demo", kicker=kicker, title=title, summary=summary, left=left, right=right,
             bullets=bullets, outcome=outcome, notes=notes)
    d.update(kw)
    return d


def O(kicker, title, summary, items, outcome=None, notes=None):
    return dict(kind="outcome", kicker=kicker, title=title, summary=summary, items=items,
                outcome=outcome, notes=notes)


def build_front():
    out = []
    out.append(dict(kind="cover",
                    kicker="AI & DATA SCIENCE · CLASSROOM SERIES",
                    title="Prompt Engineering",
                    subtitle="Beginner to Advanced",
                    lines=["AI-யுடன் தெளிவாகப் பேசக் கற்றுக்கொள் — அடிப்படையிலிருந்து advanced workflow வரை.",
                           "14 Modules · Complete Teaching Deck · Live Demos · Practice Exercises"],
                    meta="Tamil explanations  |  English technical terms  |  ChatGPT · Gemini · Copilot",
                    image="assets/cover.png",
                    notes="முதல் வகுப்பில் இந்த slide-ஐ காட்டி, course முழுவதும் 14 modules இயங்கும் என்று விளக்கவும். "
                          "இந்த deck ஒரு teacher guide ஆகவும், student workbook ஆகவும் பயன்படும்."))

    out.append(W("COURSE INTRODUCTION", "இந்த Course பற்றி என்ன?",
                 ["Prompt Engineering என்பது AI-க்கு சரியான கட்டளையை (prompt) வடிவமைக்கும் திறன் — இது ஒரு கற்றுக்கொள்ளக்கூடிய technical skill.",
                  "இந்த course-ல் 14 modules வழியாக அடிப்படையிலிருந்து advanced AI workflow வரை படிப்படியாகக் கற்போம்."],
                 {"type": "flow", "nodes": [
                     {"t": "Concept", "s": "கருத்து விளக்கம்"},
                     {"t": "Example", "s": "நிஜ உதாரணம்"},
                     {"t": "Live Demo", "s": "ChatGPT-ல் செய்து காட்டல்"},
                     {"t": "Practice", "s": "மாணவர் சுயமாக எழுதுதல்"},
                     {"t": "Assessment", "s": "பரீட்சை + project"}],
                  "caption": "ஒவ்வொரு topic-ம் இதே 5 படிநிலைகளில் கற்பிக்கப்படுகிறது."},
                 bullets=[
                     ("யாருக்கு:", "College students, beginners, AI-ஐ முதன்முறை பயன்படுத்துபவர்கள், aspiring AI professionals."),
                     ("எப்படி:", "சுருக்கமான கருத்து → உதாரணம் → copy செய்யக்கூடிய prompt → சொந்த practice."),
                     ("எதற்காக:", "தினசரி வேலையை வேகப்படுத்த, தரமான output பெற, மீண்டும் பயன்படுத்தக்கூடிய AI workflow கட்ட."),
                     ("தேவை:", "Laptop + internet + ChatGPT / Gemini account. Coding கட்டாயம் இல்லை — Python 2 modules-ல் மட்டும்.")],
                 bullets_h=1.55,
                 notes="Course-ன் எல்லை மற்றும் எதிர்பார்ப்பை இங்கே தெளிவுபடுத்தவும்: 'AI உருவாக்குவது நாம்; AI எழுதுவது அல்ல'."))

    out.append(C("LEARNING OBJECTIVES", "Learning Objectives — என்ன கற்போம்?",
                 ["Course முடிவில் நீங்கள் 12 அளவிடக்கூடிய (measurable) திறன்களைப் பெறுவீர்கள்.",
                  "ஒவ்வொரு நோக்கமும் ஒரு action verb-உடன் எழுதப்பட்டுள்ளது — அதாவது நீங்கள் செய்து காட்ட வேண்டும்."],
                 [("Identify:", "AI, Generative AI, Prompt, Prompt Engineering வேறுபாடுகளை அடையாளம் காணுதல்."),
                  ("Write:", "Role, context, constraint, output format கொண்ட structured prompt எழுதுதல்."),
                  ("Apply:", "Role, Persona, XML, JSON, Few-Shot techniques-ஐ நிஜ வேலையில் பயன்படுத்துதல்."),
                  ("Design:", "ReAct, Tree of Thoughts, Skeleton of Thoughts அணுகுமுறைகளை வடிவமைத்தல்."),
                  ("Build:", "Prompt Chaining + Dynamic Templates கொண்ட AI workflow உருவாக்குதல்."),
                  ("Evaluate:", "Prompt-ஐ சோதித்து, தரம் அளந்து, மேம்படுத்துதல்.")],
                 {"type": "stack", "layers": [
                     {"k": "BEGINNER", "v": "Module 01–04 · அடிப்படை + அமைப்பு (Role, Persona, XML)"},
                     {"k": "INTERMEDIATE", "v": "Module 05–10 · JSON, Few-Shot, ReAct, ToT, SoT, Chaining", "accent": False},
                     {"k": "ADVANCED", "v": "Module 11–14 · Templates, Concepts, Combination, Auto Prompting"}]},
                 notes="மாணவர்களை 3 குழுக்களாகப் பிரித்து, ஒவ்வொரு level-க்கும் ஒரு நோக்கத்தைச் சொல்லச் சொல்லவும்."))

    out.append(W("COURSE ROADMAP", "14 Modules — கற்றல் பாதை",
                 ["ஒவ்வொரு module-க்கும் ஒரு reference timestamp கொடுக்கப்பட்டுள்ளது — வகுப்பில் அந்த நேரத்தில் தொடங்குங்கள்.",
                  "Beginner, Intermediate, Advanced என்ற வரிசையில் திறன் வளர்கிறது; வரிசையை மாற்ற வேண்டாம்."],
                 {"type": "custom", "fn": roadmap},
                 notes="Roadmap-ஐ காட்டி, 'இன்று எங்கே இருக்கிறோம்' என்பதை ஒவ்வொரு வகுப்பின் தொடக்கத்திலும் குறிக்கவும்."))

    rows = [["Module", "Topic", "Time", "Module", "Topic", "Time"]]
    left = [("01", "Introduction", "00:00"), ("02", "Role Prompting", "03:40"),
            ("03", "Persona Prompting", "05:27"), ("04", "XML Prompting", "07:59"),
            ("05", "JSON Prompting", "10:29"), ("06", "Few-Shot Prompting", "14:25"),
            ("07", "ReAct Prompting", "16:23")]
    right = [("08", "Tree of Thoughts", "19:39"), ("09", "Skeleton of Thoughts", "22:12"),
             ("10", "Prompt Chaining", "24:55"), ("11", "Dynamic Template", "27:38"),
             ("12", "Concepts & Practices", "28:50"), ("13", "Combining Techniques", "31:39"),
             ("14", "Auto Prompting", "35:59")]
    for a, b in zip(left, right):
        rows.append([a[0], a[1], a[2], b[0], b[1], b[2]])
    out.append(W("AGENDA", "Course Agenda & Reference Timestamps",
                 ["ஒவ்வொரு topic-ன் தொடக்க நேரமும் (timestamp) கீழே உள்ளது — பதிவு செய்யப்பட்ட வகுப்புகளுக்கும் பயன்படும்.",
                  "மொத்தம் 14 modules; ஒவ்வொன்றும் தனித்தனி திறன் — எதையும் தவிர்க்க வேண்டாம்."],
                 {"type": "table", "rows": rows, "widths": [0.09, 0.29, 0.12, 0.09, 0.29, 0.12],
                  "size": 10.2, "bold_first_col": False},
                 notes="இந்த table-ஐ print செய்து மாணவர்களுக்கு handout ஆக கொடுக்கலாம்."))

    out.append(S("HOW TO TEACH THIS DECK", "ஒரு Topic-ஐ வகுப்பில் நடத்தும் முறை",
                 ["ஒவ்வொரு module-க்கும் 25–40 நிமிடங்கள் ஒதுக்குங்கள்; concept-க்கு 40%, demo-க்கு 30%, practice-க்கு 30%.",
                  "மாணவர்கள் prompt-ஐ தட்டச்சு செய்து பார்க்காமல் கற்றுக்கொள்ள முடியாது — கண்டிப்பாக practice நடத்துங்கள்."],
                 [("1. Hook (2 நிமிடம்):", "தினசரி வாழ்க்கை உதாரணத்துடன் தொடங்குங்கள்."),
                  ("2. Concept (6 நிமிடம்):", "இரண்டு வரி சுருக்கம் + bullets மட்டும்."),
                  ("3. Demo (8 நிமிடம்):", "Slide-ல் உள்ள prompt-ஐ நேரடியாக ChatGPT-ல் இயக்கிக் காட்டுங்கள்."),
                  ("4. Practice (8 நிமிடம்):", "மாணவர்கள் அதே prompt-ஐ திருத்தி மீண்டும் இயக்கட்டும்."),
                  ("5. Compare (4 நிமிடம்):", "இரண்டு மாணவர் output-ஐ ஒப்பிட்டு விவாதிக்கவும்."),
                  ("6. Outcome (2 நிமிடம்):", "கடைசி strip-ல் உள்ள திறனை ஒவ்வொருவரும் சொல்லட்டும்.")],
                 {"type": "callout", "k": "TEACHER TIPS",
                  "lines": [("பிழையும் பாடமே: ", "AI தவறாக பதில் அளித்தால், அதை மறைக்காமல் காரணத்தை விவாதியுங்கள்."),
                            ("ஒரே prompt, வேறு output: ", "temperature/randomness காரணமாக output மாறும் என்பதைக் காட்டுங்கள்."),
                            ("Tamil + English: ", "technical terms-ஐ ஆங்கிலத்திலேயே வைத்துப் பேசுங்கள் — interview-க்கு உதவும்."),
                            ("Notebook: ", "ஒவ்வொரு மாணவரும் தங்கள் சிறந்த prompt-ஐ ஒரு notebook-ல் சேமிக்கட்டும்.")]},
                 left_w=7.35, size=13, gap=9,
                 notes="இந்த slide-ஐ ஆசிரியருக்கான நடைமுறை வழிகாட்டியாகப் பயன்படுத்தவும்."))
    return out


def build_m1():
    K = "MODULE 01 · INTRODUCTION · 00:00"
    out = []
    out.append(C(K, "01 · Artificial Intelligence & Generative AI",
                 ["AI என்பது மனித நுண்ணறிவு போன்ற திறன்களை (புரிதல், முடிவெடுத்தல், கற்றல்) கணினிக்கு வழங்கும் தொழில்நுட்பம்.",
                  "Generative AI என்பது புதிய உரை, படம், code போன்ற புதிய உள்ளடக்கத்தை உருவாக்கும் AI வகையாகும்."],
                 [("AI (Artificial Intelligence):", "மொழி புரிதல், முடிவெடுத்தல், கற்றல் போன்ற மனித திறன்களை கணினியில் செயல்படுத்தும் தொழில்நுட்பம்."),
                  ("Machine Learning:", "தரவிலிருந்து (data) விதிகளைத் தானாகக் கற்றுக்கொள்ளும் AI-ன் ஒரு பிரிவு."),
                  ("Generative AI:", "பயிற்சி தரவின் அடிப்படையில் புதிய உள்ளடக்கத்தை (text, image, audio, code) உருவாக்கும் model."),
                  ("எடுத்துக்காட்டுகள்:", "ChatGPT, Gemini, Claude, Microsoft Copilot, Midjourney."),
                  ("முக்கிய கருத்து:", "AI பதிலை 'தேடி' எடுப்பதில்லை; probability அடிப்படையில் 'உருவாக்கு'கிறது.")],
                 {"type": "nested", "layers": [
                     {"t": "Artificial Intelligence (AI)", "s": "பரந்த குடை — அனைத்து அமைப்புகள்"},
                     {"t": "Machine Learning (ML)", "s": "data-விலிருந்து கற்கும் algorithm"},
                     {"t": "Deep Learning (DL)", "s": "neural network model-கள்"},
                     {"t": "Generative AI / LLM", "s": "ChatGPT, Gemini — உள்ளடக்கம் உருவாக்கும் model"}]},
                 outcome="AI, ML, Generative AI ஆகியவற்றின் உறவை விளக்கி, GenAI-ன் நிஜ பயன்பாடுகளை அடையாளம் காண முடியும்.",
                 notes="'AI = பரந்த குடை, GenAI = அதற்குள் ஒரு கிளை' என்று nested diagram-ஐ வைத்து விளக்கவும்."))

    out.append(C(K, "02 · Prompt என்றால் என்ன?",
                 ["Prompt என்பது AI-க்கு நாம் கொடுக்கும் கேள்வி அல்லது கட்டளை (input).",
                  "Prompt Engineering என்பது அந்த கட்டளையைத் தெளிவாக, கட்டமைப்பாக வடிவமைத்து மேம்படுத்தும் திறன்."],
                 [("Prompt:", "AI-க்கு அனுப்பப்படும் உரை — கேள்வி, கட்டளை, context, எடுத்துக்காட்டு எதுவும் இருக்கலாம்."),
                  ("Prompt Engineering:", "விரும்பிய output கிடைக்கும் வகையில் prompt-ஐ வடிவமைத்து, சோதித்து, மேம்படுத்தும் செயல்."),
                  ("எப்படி வேலை செய்கிறது:", "LLM 'next-token prediction' மூலம் அடுத்த சொல்லைக் கணக்கிட்டு பதிலை உருவாக்கும்."),
                  ("சிறு மாற்றம், பெரிய விளைவு:", "'Write an email' vs 'நீ ஒரு HR manager; 120 வார்த்தையில் formal email எழுது' — output முற்றிலும் வேறு."),
                  ("திறன்:", "இது coding அல்ல; தெளிவான சிந்தனையும் மொழி திறனும் தேவை.")],
                 {"type": "vflow", "steps": [
                     {"t": "Prompt (உங்கள் input)", "s": "கேள்வி + context + கட்டளைகள்"},
                     {"t": "Tokenization + context", "s": "உரை எண்களாக (token) மாற்றப்படுகிறது"},
                     {"t": "Next-token prediction", "s": "ஒவ்வொரு சொல்லாக நிகழ்தகவு அடிப்படையில் உருவாக்கல்"},
                     {"t": "Response (output)", "s": "நீங்கள் பார்க்கும் பதில் — prompt-ஐப் பொருத்தது"}]},
                 outcome="Prompt மற்றும் Prompt Engineering-ஐ வரையறுத்து, LLM எப்படி பதில் உருவாக்குகிறது என்பதை விளக்க முடியும்."))

    out.append(C(K, "03 · Prompt Engineering ஏன் முக்கியம்?",
                 ["சரியான prompt தரமான, நேரடியாகப் பயன்படுத்தக்கூடிய output-ஐ தருகிறது.",
                  "தெளிவற்ற prompt நேரத்தையும் token செலவையும் வீணாக்கி, திரும்பத் திரும்ப முயலச் செய்கிறது."],
                 [("Output தரம்:", "தேவை, context, format ஆகியவை கொடுக்கப்படும் போது பதில் தெளிவாகவும் பயனுள்ளதாகவும் இருக்கும்."),
                  ("நேரம் & செலவு:", "retry குறைகிறது; API பயன்பாட்டில் token cost-ம் குறைகிறது."),
                  ("நிலைத்தன்மை (Consistency):", "ஒரே template பயன்படுத்தினால் பல நாட்களிலும் ஒரே தரம் கிடைக்கும்."),
                  ("தவறுகள் குறைவு:", "தேவையான data-வைக் கொடுத்தால் hallucination (புனையப்பட்ட பதில்) குறைகிறது."),
                  ("குழு உற்பத்தித்திறன்:", "சிறந்த prompt-களை prompt library ஆகச் சேமித்து குழுவுடன் பகிரலாம்.")],
                 {"type": "table", "rows": [
                     ["Prompt வகை", "கிடைக்கும் Output", "சரிசெய்யும் நேரம்"],
                     ["\"Write about AI\"", "பொதுவான, யாருக்கும் பயன்படாத உரை", "10–15 நிமிடம்"],
                     ["\"Write 200 words on AI for college students\"", "ஓரளவு பயனுள்ள உரை", "5 நிமிடம்"],
                     ["Role + audience + format + constraints", "நேரடியாகப் பயன்படுத்தக்கூடிய output", "1–2 நிமிடம்"]],
                  "widths": [0.42, 0.34, 0.24], "size": 9.8},
                 outcome="Prompt-ன் தரம் output-ஐ எப்படிப் பாதிக்கிறது என்பதை ஒப்பிட்டு விளக்க முடியும்."))

    out.append(C(K, "04 · ஒரு நல்ல Prompt-ன் அமைப்பு",
                 ["நல்ல prompt-ல் ஆறு கூறுகள் இருக்கும்: Role, Task, Context, Constraints, Output format, Examples.",
                  "இந்த ஆறு கூறுகளும் AI-ன் ஊகங்களை (assumptions) குறைத்து, தேவையான பதிலை நோக்கி வழிகாட்டுகின்றன."],
                 [("Role:", "AI எந்த நிபுணராக பதில் அளிக்க வேண்டும்."),
                  ("Task:", "சரியாக என்ன செய்ய வேண்டும் — ஒரே வாக்கியத்தில்."),
                  ("Context:", "பின்னணி தகவல் — யாருக்கு, எதற்காக, என்ன data."),
                  ("Constraints:", "எல்லை — நீளம், மொழி, tone, எதைச் சேர்க்கக் கூடாது."),
                  ("Output Format:", "table / JSON / bullet / email — எப்படி வேண்டும்."),
                  ("Examples (optional):", "ஒன்று அல்லது இரண்டு மாதிரி input–output.")],
                 {"type": "code", "label": "prompt.txt  ·  ஆறு கூறுகள் குறிக்கப்பட்டவை", "lines": [
                     "# 1. ROLE",
                     "You are a senior HR manager at Zeta Tech.",
                     "# 2. TASK",
                     "Write a welcome email for a new joiner.",
                     "# 3. CONTEXT",
                     "Name: Arun | Role: Junior Developer | Start: 01 Dec 2026",
                     "# 4. CONSTRAINTS",
                     "Max 120 words, formal tone, no emoji, no salary details.",
                     "# 5. OUTPUT FORMAT",
                     "Subject line + greeting + 2 paragraphs + signature.",
                     "# 6. EXAMPLE (optional)",
                     "Subject: Welcome to Zeta Tech, Arun!"]},
                 outcome="Role, Task, Context, Constraints, Format, Examples ஆகிய ஆறு கூறுகளைப் பயன்படுத்தி prompt எழுத முடியும்.",
                 size=13, gap=8))

    out.append(W(K, "05 · Basic Prompt vs Effective Prompt",
                 ["Basic prompt ஒரு தலைப்பை மட்டும் சொல்கிறது; AI தன் ஊகத்தில் பதிலை உருவாக்குகிறது.",
                  "Effective prompt யார், யாருக்கு, எப்படி, எவ்வளவு என்பதைத் தெளிவாகக் குறிப்பிடுகிறது."],
                 {"type": "compare", "panels": [
                     {"label": "Basic Prompt", "tag": "INPUT", "kind": "bad", "mono": True,
                      "lines": ["Write an email.", "", "OUTPUT:",
                                "Dear Sir/Madam,", "I am writing this email to inform...",
                                "", "-> No audience, no goal",
                                "-> Generic, unusable text"]},
                     {"label": "Effective Prompt", "tag": "INPUT", "kind": "good", "mono": True,
                      "lines": ["You are an HR manager at Zeta Tech.",
                                "Write a welcome email to Arun,",
                                "Junior Developer, joining 01 Dec.",
                                "120 words, formal, no emoji.",
                                "Subject + body + signature.",
                                "", "OUTPUT:",
                                "-> A ready-to-send professional email",
                                "-> Usable in a single attempt"]}]},
                 outcome="இரண்டு prompt-களை ஒப்பிட்டு, ஏன் ஒன்று சிறந்த output தருகிறது என்பதை விளக்க முடியும்.",
                 notes="இரண்டு prompt-ஐயும் நேரடியாக ChatGPT-ல் இயக்கி, output-ஐ பக்கத்துடன் ஒப்பிடக் காட்டவும்."))

    out.append(D(K, "06 · Practical Demo — Professional Email Prompt",
                 ["கீழே உள்ள prompt-ஐ அப்படியே copy செய்து ChatGPT அல்லது Gemini-ல் இயக்குங்கள்.",
                  "Role + context + constraint + format இருப்பதால் output நேரடியாகப் பயன்படுத்தக்கூடியதாக வரும்."],
                 {"type": "code", "label": "INPUT PROMPT", "lines": [
                     "You are a senior HR manager at Zeta Tech.",
                     "",
                     "TASK: Write a welcome email for a new joiner.",
                     "CONTEXT:",
                     "- Name: Arun Kumar",
                     "- Role: Junior Developer",
                     "- Start date: 01 December 2026",
                     "- Reporting manager: Priya (Team Lead)",
                     "",
                     "CONSTRAINTS:",
                     "- Maximum 120 words",
                     "- Formal but warm tone, no emoji",
                     "- Mention first-day reporting time 9:30 AM",
                     "",
                     "OUTPUT FORMAT:",
                     "Subject line + greeting + 2 short paragraphs + signature"]},
                 {"type": "code", "label": "EXPECTED OUTPUT", "lines": [
                     "Subject: Welcome to Zeta Tech, Arun!",
                     "",
                     "Dear Arun,",
                     "",
                     "Welcome to Zeta Tech! We are delighted that you",
                     "are joining us as a Junior Developer on",
                     "01 December 2026.",
                     "",
                     "Please report at 9:30 AM to the reception desk.",
                     "Your reporting manager, Priya (Team Lead), will",
                     "guide you through onboarding.",
                     "",
                     "We look forward to working with you.",
                     "",
                     "Warm regards,",
                     "HR Team, Zeta Tech"]},
                 outcome="ஒரு prompt-ஐ role, context, constraint, format உடன் எழுதி, professional email output பெற முடியும்.",
                 notes="மாணவர்களை இரண்டு குழுவாகப் பிரித்து, ஒரு குழு basic prompt-ஐயும் மற்றொரு குழு effective prompt-ஐயும் இயக்கி output-ஐ ஒப்பிடச் சொல்லவும்."))

    out.append(W(K, "07 · Real-World Applications",
                 ["Prompt Engineering இன்று கிட்டத்தட்ட ஒவ்வொரு துறையிலும் பயன்படுகிறது.",
                  "கீழே உள்ள ஆறு பயன்பாடுகளும் மாணவர்கள் இப்போதே முயற்சி செய்யக்கூடியவை."],
                 {"type": "cards", "cols": 3, "cards": [
                     {"k": "EDUCATION", "t": "பாட விளக்கம் & கேள்வி உருவாக்கம்", "s": "ஒரே பாடத்தை வெவ்வேறு நிலைகளுக்கு ஏற்ப விளக்கவும், MCQ உருவாக்கவும்."},
                     {"k": "SOFTWARE", "t": "Code generation & debugging", "s": "Function எழுதுதல், error விளக்கம், unit test உருவாக்குதல்."},
                     {"k": "BUSINESS", "t": "Email, report, proposal", "s": "வாடிக்கையாளர் email, விற்பனை அறிக்கை, meeting notes சுருக்கம்."},
                     {"k": "SUPPORT", "t": "Ticket classification & reply", "s": "Priority அடையாளம், தானியங்கி பதில் draft, sentiment analysis."},
                     {"k": "DATA", "t": "Analysis & summarization", "s": "நீண்ட அறிக்கையை சுருக்கம், table-ஐ insight ஆக மாற்றுதல்."},
                     {"k": "IT OPS", "t": "Troubleshooting & monitoring", "s": "Server பிழை தீர்வு படிகள், log விளக்கம், runbook உருவாக்கம்."}]},
                 bullets=["இவை அனைத்திற்கும் அடிப்படை ஒன்றே — தெளிவான, கட்டமைக்கப்பட்ட கட்டளை."],
                 bullets_h=0.5,
                 outcome="தங்கள் துறையில் Prompt Engineering-ஐ எங்கே பயன்படுத்தலாம் என்பதை அடையாளம் காண முடியும்."))

    out.append(O(K, "Module 01 — Learning Outcome",
                 ["இந்த module-ல் AI-ன் அடிப்படை, prompt-ன் அர்த்தம், நல்ல prompt-ன் அமைப்பு ஆகியவற்றைக் கற்றோம்.",
                  "இனி நீங்கள் எழுதும் ஒவ்வொரு prompt-ஐயும் ஆறு கூறுகளுடன் எழுதிப் பழகுங்கள்."],
                 ["AI, Machine Learning, Generative AI ஆகியவற்றை வேறுபடுத்தி விளக்க முடியும்.",
                  "Prompt மற்றும் Prompt Engineering-ஐ வரையறுக்க முடியும்.",
                  "Prompt-ன் தரம் output-ஐ எப்படிப் பாதிக்கிறது என்று ஒப்பிட்டுக் காட்ட முடியும்.",
                  "Role, Task, Context, Constraints, Format, Examples ஆகிய ஆறு கூறுகளைப் பயன்படுத்தி prompt எழுத முடியும்.",
                  "Basic prompt-ஐ effective prompt ஆக மாற்றி எழுத முடியும்.",
                  "தங்கள் துறையில் Prompt Engineering-ன் பயன்பாடுகளைப் பட்டியலிட முடியும்."],
                 outcome="Module 01 நிறைவு — அடுத்து Role Prompting (03:40).",
                 notes="மாணவர்களை ஒவ்வொரு நோக்கத்திற்கும் ஒரு வாக்கிய எடுத்துக்காட்டு சொல்லச் சொல்லவும்."))
    return out


def build_m2():
    K = "MODULE 02 · ROLE PROMPTING · 03:40"
    out = []
    out.append(C(K, "01 · Role Prompting என்றால் என்ன?",
                 ["Role Prompting என்பது AI-க்கு ஒரு நிபுணர் வேடத்தை (role) கொடுத்து பதில் கேட்பது.",
                  "அந்த role-ன் அறிவு, சொற்கள், முன்னுரிமைகள் ஆகியவற்றின் அடிப்படையில் AI பதில் அளிக்கும்."],
                 [("வரையறை:", "'Act as a …' / 'You are a …' என்று தொடங்கி AI-க்கு ஒரு professional அடையாளத்தைக் கொடுப்பது."),
                  ("ஏன் role?", "AI-ன் பதில் அனைத்து துறைகளுக்கும் பொதுவானதாக இருக்காமல், குறிப்பிட்ட துறைக்கு ஏற்ப ஆழமாக அமையும்."),
                  ("எப்படி வேலை செய்கிறது:", "Role, பயிற்சி தரவில் உள்ள அந்தத் துறையின் சொற்களையும் வடிவங்களையும் (patterns) செயல்படுத்துகிறது."),
                  ("முக்கியம்:", "Role மட்டும் போதாது — task, context, output format-ஐயும் சேர்க்க வேண்டும்."),
                  ("எச்சரிக்கை:", "Role ஒரு 'போலி அதிகாரம்' அல்ல; தவறான தகவலை சரிபார்க்க வேண்டியது நமது பொறுப்பு.")],
                 {"type": "vflow", "steps": [
                     {"t": "Role சொல்லுதல்", "s": "'You are a network engineer…'"},
                     {"t": "Domain சொற்கள் & முன்னுரிமை", "s": "AI அந்தத் துறை பாணியில் சிந்திக்கிறது"},
                     {"t": "Task + context", "s": "உங்கள் பிரச்சினையை அந்தக் கண்ணோட்டத்தில் பார்க்கிறது"},
                     {"t": "Role-க்கு ஏற்ற output", "s": "சரியான ஆழம், சரியான சொற்கள், சரியான படிகள்"}]},
                 outcome="Role Prompting-ஐ வரையறுத்து, ஏன் role கொடுப்பது output-ஐ மாற்றுகிறது என்பதை விளக்க முடியும்."))

    out.append(C(K, "02 · Role சொல்வதால் என்ன மாறுகிறது?",
                 ["Role, AI-ன் சொற்களஞ்சியம், ஆழம், முன்னுரிமை ஆகியவற்றை மாற்றுகிறது.",
                  "ஒரே கேள்விக்கு வெவ்வேறு role-கள் வெவ்வேறு கோணங்களில் பதில் தரும்."],
                 [("சொற்களஞ்சியம் (Vocabulary):", "developer 'function, API, commit' என்பார்; network engineer 'VLAN, latency, firewall' என்பார்."),
                  ("ஆழம் (Depth):", "beginner-க்கு எளிமையாக, expert-க்கு technical ஆக."),
                  ("முன்னுரிமை (Priority):", "security expert முதலில் risk-ஐப் பேசுவார்; developer முதலில் implementation-ஐப் பேசுவார்."),
                  ("Format:", "doctor-க்கு checklist, teacher-க்கு step-by-step, analyst-க்கு table."),
                  ("பொறுப்பு உணர்வு:", "'senior' role கொடுத்தால் AI caveats, edge cases-ஐயும் சேர்த்துப் பேசும்.")],
                 {"type": "table", "rows": [
                     ["கேள்வி", "Role இல்லாமல்", "Role உடன் (Network Engineer)"],
                     ["\"Server slow ஆகிறது\"", "RAM அதிகரிக்கவும், restart செய்யவும்", "Latency, packet loss, bandwidth, switch load — படிப்படியாக பரிசோதிக்கவும்"],
                     ["\"Password policy\"", "வலுவான password வைக்கவும்", "NIST 800-63B அடிப்படையில் length, MFA, lockout policy"]],
                  "widths": [0.26, 0.30, 0.44], "size": 9.6},
                 outcome="Role, பதிலின் சொற்கள், ஆழம், முன்னுரிமையை எப்படி மாற்றுகிறது என்பதை ஒப்பிட்டு விளக்க முடியும்."))

    out.append(W(K, "03 · பயன்படும் Professional Roles",
                 ["ஒவ்வொரு துறைக்கும் ஒரு role template தயார் செய்து வைத்தால், தினசரி வேலை வேகமாகும்.",
                  "கீழே உள்ள ஆறு role-கள் மாணவர்கள் அடிக்கடி பயன்படுத்தக்கூடியவை."],
                 {"type": "cards", "cols": 3, "cards": [
                     {"k": "SOFTWARE", "t": "Act as a Software Developer", "s": "Code, debugging, architecture, code review, unit tests."},
                     {"k": "NETWORK", "t": "Act as a Network Engineer", "s": "Routing, switching, latency, firewall, subnetting."},
                     {"k": "SECURITY", "t": "Act as a Cybersecurity Expert", "s": "Threat model, OWASP, incident response, hardening."},
                     {"k": "DATA", "t": "Act as a Data Analyst", "s": "SQL, dashboard, trend, KPI விளக்கம்."},
                     {"k": "TEACHING", "t": "Act as a College Professor", "s": "பாட விளக்கம், MCQ, assignment, rubric."},
                     {"k": "BUSINESS", "t": "Act as a Business Analyst", "s": "Requirement, process flow, stakeholder email."}]},
                 bullets=["இந்தப் பட்டியலை விரிவுபடுத்தி, உங்கள் துறைக்கான role-ஐயும் சேர்க்கவும்."],
                 bullets_h=0.5,
                 outcome="தங்கள் தேவைக்கு ஏற்ற professional role-ஐத் தேர்ந்தெடுத்து prompt-ல் பயன்படுத்த முடியும்."))

    out.append(S(K, "04 · சிறந்த Role Prompt எழுதும் வழி",
                 ["Role-ஐ முடிந்தவரை குறிப்பாக (specific) எழுதுங்கள் — 'expert' மட்டும் போதாது.",
                  "Role + task + context + format ஆகிய நான்கும் சேர்ந்தால் மட்டுமே சிறந்த output கிடைக்கும்."],
                 [("Seniority சேர்க்கவும்:", "'senior network engineer with 10 years in data centre operations'."),
                  ("Domain சேர்க்கவும்:", "எந்தத் துறை, எந்தச் சூழல் என்பதைக் குறிப்பிடுங்கள்."),
                  ("Task-ஐ தனியாக எழுதுங்கள்:", "Role-ஐ task-உடன் கலக்காமல் வெவ்வேறு வரிகளில்."),
                  ("Format கேளுங்கள்:", "table, checklist, runbook, JSON — எப்படி வேண்டும் என்று."),
                  ("Audience சொல்லுங்கள்:", "பதில் யாருக்கு — beginner, manager, client."),
                  ("சரிபார்க்கவும்:", "Role கொடுத்தாலும் தவறான தகவல் வரலாம்; மூல ஆதாரத்துடன் ஒப்பிடுங்கள்.")],
                 {"type": "compare", "panels": [
                     {"label": "பலவீனமான Role", "kind": "bad", "mono": True, "code_label": "prompt.txt",
                      "lines": ["Act as an IT expert.", "Fix the server problem."]},
                     {"label": "வலுவான Role", "kind": "good", "mono": True, "code_label": "prompt.txt",
                      "lines": ["You are a senior Windows Server",
                                "administrator (10+ years) in a",
                                "bank data centre.",
                                "TASK: Diagnose why a Windows",
                                "Server 2019 VM reboots randomly.",
                                "CONTEXT: 40 VMs, Hyper-V, event",
                                "log 1074 shows unknown reason.",
                                "OUTPUT: numbered checklist with",
                                "commands + escalation criteria."]}]},
                 outcome="குறிப்பான role, seniority, domain, audience ஆகியவற்றுடன் Role Prompt எழுத முடியும்.",
                 left_w=4.55))

    out.append(W(K, "05 · Practical Demo — ஒரே கேள்வி, மூன்று Role-கள்",
                 ["கீழே உள்ள ஒரே கேள்வியை மூன்று வெவ்வேறு role-களுடன் கேட்கிறோம்.",
                  "Output-ன் சொற்கள், கட்டமைப்பு, முன்னுரிமை எப்படி மாறுகிறது என்பதைக் கவனியுங்கள்."],
                 {"type": "compare", "panels": [
                     {"label": "Software Developer", "tag": "PROMPT", "kind": "good", "mono": True,
                      "code_label": "prompt.txt",
                      "lines": ["You are a senior software developer.",
                                "Our web app is 'slow'. List the",
                                "first 5 things you would check.",
                                "OUTPUT: 1) Query performance / N+1",
                                "2) API response time & logs",
                                "3) Caching strategy",
                                "4) Frontend bundle size",
                                "5) DB indexes & connection pool"]},
                     {"label": "Network Engineer", "tag": "PROMPT", "kind": "good", "mono": True,
                      "code_label": "prompt.txt",
                      "lines": ["You are a network engineer.",
                                "Our web app is 'slow'. List the",
                                "first 5 things you would check.",
                                "OUTPUT: 1) Latency / packet loss",
                                "2) DNS resolution time",
                                "3) Bandwidth & firewall rules",
                                "4) Switch & load balancer health",
                                "5) Wireshark capture analysis"]},
                     {"label": "Cybersecurity Expert", "tag": "PROMPT", "kind": "good", "mono": True,
                      "code_label": "prompt.txt",
                      "lines": ["You are a cybersecurity expert.",
                                "Our web app is 'slow'. List the",
                                "first 5 things you would check.",
                                "OUTPUT: 1) Traffic spike / DDoS",
                                "2) Resource exhaustion (mining)",
                                "3) Suspicious logins",
                                "4) WAF & rate-limit alerts",
                                "5) Recent config changes"]}]},
                 outcome="ஒரே பிரச்சினைக்கு வெவ்வேறு role-கள் வெவ்வேறு கோணங்களைத் தரும் என்பதை நிரூபித்துக் காட்ட முடியும்.",
                 notes="மூன்று prompt-ஐயும் வகுப்பில் ஒன்றன் பின் ஒன்றாக இயக்கி, 'எந்த role உங்களுக்கு பயனுள்ளது?' என்று கேளுங்கள்."))

    out.append(O(K, "06 · Module 02 — Learning Outcome",
                 ["Role Prompting என்பது AI-க்கு ஒரு தொழில் அடையாளத்தைக் கொடுத்து, அந்தக் கண்ணோட்டத்தில் பதில் பெறுவது.",
                  "Role + task + context + format சேர்ந்தால் மட்டுமே நம்பகமான, பயன்படுத்தக்கூடிய output கிடைக்கும்."],
                 ["Role Prompting-ஐ வரையறுத்து விளக்க முடியும்.",
                  "Role இருப்பதற்கும் இல்லாததற்கும் உள்ள வேறுபாட்டை ஒப்பிட முடியும்.",
                  "Software, Network, Security போன்ற துறைகளுக்கான role-ஐத் தேர்ந்தெடுக்க முடியும்.",
                  "Seniority, domain, audience ஆகியவற்றுடன் குறிப்பான role prompt எழுத முடியும்.",
                  "ஒரே கேள்வியை மூன்று role-களில் கேட்டு output-ஐ ஒப்பிட்டு பகுப்பாய்வு செய்ய முடியும்.",
                  "Role-ஐ task, constraint, output format உடன் இணைத்து prompt உருவாக்க முடியும்."],
                 outcome="Module 02 நிறைவு — அடுத்து Persona Prompting (05:27)."))
    return out
