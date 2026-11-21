# -*- coding: utf-8 -*-
"""Course summary, project, final outcomes, assessment, conclusion."""
from .content_a import C, W, S, D, O


def slides():
    out = []
    out.append(W("COURSE SUMMARY", "14 Techniques — ஒரே பார்வையில்",
                 ["ஒவ்வொரு technique-ம் ஒரு குறிப்பிட்ட பிரச்சினைக்கான கருவி.",
                  "எந்த வேலைக்கு எந்தக் கருவி என்பதை நினைவில் வைத்தால் போதும்."],
                 {"type": "grid", "cols": 5, "cells": [
                     {"n": "01", "t": "Introduction", "s": "AI · Prompt · அமைப்பு"},
                     {"n": "02", "t": "Role", "s": "நிபுணர் வேடம்"},
                     {"n": "03", "t": "Persona", "s": "tone + audience"},
                     {"n": "04", "t": "XML", "s": "எல்லை தெளிவு"},
                     {"n": "05", "t": "JSON", "s": "machine-readable"},
                     {"n": "06", "t": "Few-Shot", "s": "உதாரணங்கள்"},
                     {"n": "07", "t": "ReAct", "s": "tools + சிந்தனை"},
                     {"n": "08", "t": "Tree of Thoughts", "s": "பல வழிகள்"},
                     {"n": "09", "t": "Skeleton of Thoughts", "s": "outline + விரிவு"},
                     {"n": "10", "t": "Chaining", "s": "படிநிலை workflow"},
                     {"n": "11", "t": "Dynamic Template", "s": "மீள்பயன் prompt"},
                     {"n": "12", "t": "Concepts", "s": "தரம் + சோதனை"},
                     {"n": "13", "t": "Combining", "s": "கலந்த அணுகுமுறை"},
                     {"n": "14", "t": "Auto Prompting", "s": "AI எழுதும் prompt"}]},
                 outcome="14 technique-களையும் பெயரிட்டு, ஒவ்வொன்றின் பயன்பாட்டைச் சொல்ல முடியும்."))

    out.append(W("TECHNIQUE SELECTION GUIDE", "எந்த வேலைக்கு எந்த Technique?",
                 ["நிஜ வேலையில் 'எந்த technique?' என்ற கேள்வி அடிக்கடி வரும்.",
                  "இந்த அட்டவணையை ஒரு cheat sheet ஆகப் பயன்படுத்துங்கள்."],
                 {"type": "table", "rows": [
                     ["உங்கள் வேலை", "Technique", "ஏன்"],
                     ["நிபுணர் போன்ற பதில் வேண்டும்", "Role + Persona", "அறிவு + tone"],
                     ["பல பகுதி கட்டளைகள்", "XML", "எல்லை தெளிவு"],
                     ["App-ல் பயன்படுத்த வேண்டும்", "JSON (+ schema)", "parse செய்ய எளிது"],
                     ["வகைப்படுத்த வேண்டும்", "Few-Shot + JSON", "label + வடிவம்"],
                     ["நடப்பு தரவு தேவை", "ReAct + tools", "உண்மைத் தகவல்"],
                     ["பல வழிகளில் முடிவெடுக்க", "Tree of Thoughts", "ஒப்பீடு"],
                     ["பெரிய ஆவணம் / website", "Skeleton of Thoughts", "அமைப்பு"],
                     ["பல படி வேலை", "Prompt Chaining", "துல்லியம்"],
                     ["அடிக்கடி திரும்பச் செய்யும் வேலை", "Dynamic Template", "மீள்பயன்"],
                     ["Prompt-ஐ மேம்படுத்த", "Auto Prompting", "விரைவு"]],
                  "widths": [0.38, 0.32, 0.30], "size": 9.6},
                 outcome="ஒரு புதிய வேலைக்கு சரியான technique-ஐத் தேர்ந்தெடுக்க முடியும்."))

    out.append(W("PRACTICAL PROJECT", "Project — AI-Based IT Support Assistant",
                 ["இந்த project-ல் 14 module-களின் திறன்களை ஒரே அமைப்பில் இணைப்பீர்கள்.",
                  "இது மதிப்பீட்டிற்கான முக்கிய வேலை — தனியாகவோ 3 பேர் குழுவாகவோ செய்யலாம்."],
                 {"type": "cards", "cols": 3, "cards": [
                     {"k": "GOAL", "t": "Ticket to பதில்", "s": "IT support ticket-ஐ புரிந்து, வகைப்படுத்தி, பதில் draft செய்யும் assistant."},
                     {"k": "TECHNIQUES", "t": "6 techniques", "s": "Role, Persona, XML, Few-Shot, JSON, Chaining."},
                     {"k": "INPUT", "t": "10 test tickets", "s": "Critical, Normal, Low, edge cases — கைப்பட எழுதுங்கள்."},
                     {"k": "OUTPUT", "t": "JSON + email", "s": "category, priority, needs_human, reply_draft."},
                     {"k": "DELIVERABLES", "t": "5 items", "s": "Architecture, 4 prompts, schema, outputs, report."},
                     {"k": "EVALUATION", "t": "Rubric", "s": "Accuracy 30, format 20, tone 20, testing 20, docs 10."}]},
                 outcome="Project-ன் இலக்கு, உள்ளீடு, வெளியீடு, மதிப்பீட்டு முறையை விளக்க முடியும்."))

    out.append(W("PROJECT STEPS", "Project-ஐ 5 கட்டங்களாகச் செய்யுங்கள்",
                 ["ஒவ்வொரு கட்டத்திற்கும் ஒரு வாரம் ஒதுக்கினால் 5 வாரத்தில் முடிக்கலாம்.",
                  "ஒவ்வொரு கட்டத்தின் முடிவையும் ஆசிரியரிடம் காட்டி உறுதிப்படுத்துங்கள்."],
                 {"type": "table", "rows": [
                     ["கட்டம்", "செய்ய வேண்டியது", "வெளியீடு"],
                     ["1. Plan", "Ticket வகைகள், SLA, JSON schema", "schema.json"],
                     ["2. Prompt design", "Role + Persona + XML prompt", "stage1.txt"],
                     ["3. Few-Shot", "ஒவ்வொரு label-க்கும் 2 examples", "examples.md"],
                     ["4. Chain + Template", "4 stage workflow + email template", "workflow diagram"],
                     ["5. Test & report", "10 ticket-ல் இயக்கி மதிப்பெண்", "report.md"]],
                  "widths": [0.20, 0.50, 0.30], "size": 10.2},
                 outcome="Project-ஐ ஐந்து கட்டங்களாகத் திட்டமிட்டு நிறைவேற்ற முடியும்."))

    out.append(O("FINAL LEARNING OUTCOMES", "Course முடிவில் நீங்கள் என்ன செய்ய முடியும்?",
                 ["இந்த 12 திறன்களும் course-ன் ஒட்டுமொத்த விளைவு.",
                  "ஒவ்வொன்றையும் செய்து காட்ட முடிந்தால், நீங்கள் course-ஐ முழுமையாக முடித்துள்ளீர்கள்."],
                 ["Prompt Engineering-ன் அடிப்படைகளை விளக்க முடியும்.",
                  "கட்டமைக்கப்பட்ட, பயனுள்ள prompt எழுத முடியும்.",
                  "Role & Persona prompting பயன்படுத்த முடியும்.",
                  "XML மற்றும் JSON அடிப்படையிலான prompt உருவாக்க முடியும்.",
                  "Few-Shot prompting பயன்படுத்த முடியும்.",
                  "ReAct மற்றும் tool-using AI workflow புரிந்து விளக்க முடியும்.",
                  "Tree of Thoughts, Skeleton of Thoughts அணுகுமுறைகளைப் பயன்படுத்த முடியும்.",
                  "Prompt Chaining workflow வடிவமைக்க முடியும்.",
                  "மீள்பயன் Dynamic Prompt Templates உருவாக்க முடியும்.",
                  "பல prompting techniques-ஐ இணைக்க முடியும்.",
                  "AI மூலம் prompt உருவாக்கி மேம்படுத்த முடியும்.",
                  "நடைமுறை AI-assisted workflow கட்ட முடியும்."],
                 outcome="12 திறன்களையும் சொந்தமாகச் செய்து காட்ட முடியும்.",
                 notes="இந்த slide-ஐ rubric ஆகப் பயன்படுத்தி இறுதி மதிப்பீடு செய்யலாம்."))

    out.append(W("FINAL ASSESSMENT", "Final Assessment — அமைப்பு",
                 ["மதிப்பீடு நான்கு பகுதிகளாக உள்ளது: MCQ, short answers, practical exercises, mini project.",
                  "மொத்தம் 100 மதிப்பெண்; திறன் அடிப்படையில் மதிப்பிடப்படும்."],
                 {"type": "table", "rows": [
                     ["பகுதி", "எண்ணிக்கை", "மதிப்பெண்", "நேரம்"],
                     ["Multiple Choice Questions", "10", "20", "15 நிமிடம்"],
                     ["Short Answer Questions", "5", "20", "20 நிமிடம்"],
                     ["Practical Prompt Exercises", "3", "30", "40 நிமிடம்"],
                     ["Mini Project", "1", "30", "1 வாரம்"],
                     ["மொத்தம்", "19", "100", "—"]],
                  "widths": [0.44, 0.18, 0.18, 0.20], "size": 10.6},
                 bullets=["அனுமதிக்கப்பட்டவை: குறிப்புகள், ChatGPT/Gemini (practical பகுதியில்). தடை: நேரடி copy-paste மட்டும்."],
                 bullets_h=0.45,
                 outcome="மதிப்பீட்டின் அமைப்பையும் மதிப்பெண் பங்கீட்டையும் விளக்க முடியும்."))

    out.append(W("ASSESSMENT · MCQ", "Multiple Choice — கேள்வி 1–5",
                 ["ஒவ்வொரு கேள்விக்கும் ஒரு சரியான விடை மட்டும்.",
                  "சரியான விடையை எழுத்துடன் (a/b/c/d) எழுதுங்கள்."],
                 {"type": "table", "rows": [
                     ["#", "கேள்வி", "விருப்பங்கள்"],
                     ["1", "Prompt Engineering என்பது?", "a) AI model உருவாக்குதல்  b) AI-க்கு கட்டளையை வடிவமைத்தல்  c) GPU வேகப்படுத்தல்  d) database design"],
                     ["2", "Role prompting-ல் முக்கியமானது?", "a) நீண்ட prompt  b) AI-க்கு நிபுணர் வேடம்  c) emoji  d) விலை"],
                     ["3", "Persona எதை வரையறுக்கிறது?", "a) model size  b) tone மற்றும் audience  c) API key  d) token limit"],
                     ["4", "XML prompt-ல் தவறு எது?", "a) <role>…</role>  b) nesting  c) மூடும் tag விடுவது  d) <context>"],
                     ["5", "சரியான JSON எது?", "a) {\"a\": 1}  b) {'a': 1}  c) {a: 1}  d) {a = 1}"]],
                  "widths": [0.06, 0.28, 0.66], "size": 9.4, "bold_first_col": False},
                 outcome="Prompt Engineering அடிப்படைகள் பற்றிய MCQ-க்கு விடையளிக்க முடியும்."))

    out.append(W("ASSESSMENT · MCQ", "Multiple Choice — கேள்வி 6–10",
                 ["கேள்விகள் 1–5-ஐப் போலவே, ஒரு சரியான விடை மட்டும்.",
                  "பதில்களைத் தனித்தாளில் எழுதுங்கள்."],
                 {"type": "table", "rows": [
                     ["#", "கேள்வி", "விருப்பங்கள்"],
                     ["6", "Few-Shot prompting-ல் வழக்கமான எடுத்துக்காட்டு எண்ணிக்கை?", "a) 0  b) 1  c) 3–5  d) 20"],
                     ["7", "ReAct-ல் Observation என்றால் என்ன?", "a) பயனர் கேள்வி  b) tool திருப்பிய முடிவு  c) இறுதி பதில்  d) model weight"],
                     ["8", "Tree of Thoughts எப்போது பொருத்தம்?", "a) ஒற்றை fact  b) மொழிபெயர்ப்பு  c) பல வழிகள் உள்ள பெரிய முடிவு  d) grammar correction"],
                     ["9", "Skeleton of Thoughts-ல் முதலில் என்ன உருவாக்க வேண்டும்?", "a) முழு உரை  b) outline  c) JSON  d) code"],
                     ["10", "Prompt chaining-ல் அடுத்த stage-க்கு என்ன செல்கிறது?", "a) முந்தைய stage-ன் output  b) model weights  c) API key  d) எதுவும் இல்லை"]],
                  "widths": [0.06, 0.30, 0.64], "size": 9.4, "bold_first_col": False},
                 outcome="10 MCQ-களுக்கும் சரியான விடையைத் தேர்ந்தெடுக்க முடியும்."))

    out.append(W("ASSESSMENT · SHORT ANSWERS", "Short Answer — 5 கேள்விகள்",
                 ["ஒவ்வொரு விடையும் 3–5 வாக்கியங்களில் இருக்க வேண்டும்.",
                  "தேவைப்பட்டால் ஒரு சிறு உதாரணம் அல்லது diagram சேர்க்கலாம்."],
                 {"type": "table", "rows": [
                     ["#", "கேள்வி", "மதிப்பெண்"],
                     ["1", "Role மற்றும் Persona வேறுபாட்டை 2 வாக்கியத்தில் விளக்குங்கள்.", "4"],
                     ["2", "XML prompt-ன் 2 நன்மைகளையும் 2 வரம்புகளையும் எழுதுங்கள்.", "4"],
                     ["3", "Few-Shot-ல் நல்ல எடுத்துக்காட்டுகளின் 3 பண்புகளை எழுதுங்கள்.", "4"],
                     ["4", "ReAct workflow-ன் 5 நிலைகளை வரிசையாக எழுதுங்கள்.", "4"],
                     ["5", "Dynamic template-ல் variables எப்படி வேலை செய்கிறது? உதாரணம் தருங்கள்.", "4"]],
                  "widths": [0.06, 0.79, 0.15], "size": 10.2, "bold_first_col": False},
                 outcome="ஒவ்வொரு technique-ஐயும் சொந்த வார்த்தையில் விளக்க முடியும்."))

    out.append(W("ASSESSMENT · PRACTICAL", "Practical Exercises — 3 பயிற்சிகள்",
                 ["ஒவ்வொரு பயிற்சியையும் ChatGPT/Gemini-ல் இயக்கி, output-ஐ சமர்ப்பிக்க வேண்டும்.",
                  "Prompt + output + 3 வரி விளக்கம் — மூன்றும் தேவை."],
                 {"type": "cards", "cols": 3, "cards": [
                     {"k": "EXERCISE 1 · 10 மதிப்பெண்", "t": "Structured email prompt",
                      "s": "உங்கள் கல்லூரி fest-க்கு sponsor கேட்கும் email-க்கு ஆறு கூறுகளுடன் prompt எழுதுங்கள். Output-ஐயும் சேர்க்கவும்."},
                     {"k": "EXERCISE 2 · 10 மதிப்பெண்", "t": "XML troubleshooting prompt",
                      "s": "Server slow / disk full பிரச்சினைக்கு <role>, <context>, <task>, <constraints>, <output_format> கொண்ட prompt."},
                     {"k": "EXERCISE 3 · 10 மதிப்பெண்", "t": "Few-Shot + JSON",
                      "s": "மாணவர் feedback-ஐ Positive / Negative / Suggestion என்று வகைப்படுத்த 3 examples + JSON output schema."}]},
                 outcome="மூன்று practical prompt-களைத் தனியாக எழுதி இயக்க முடியும்."))

    out.append(W("ASSESSMENT · MINI PROJECT", "Mini Project — AI IT Support Assistant",
                 ["இது course-ன் இறுதி வேலை — அனைத்து technique-களையும் இணைக்க வேண்டும்.",
                  "தனியாகவோ 3 பேர் குழுவாகவோ செய்யலாம்; குழு உறுப்பினர்களின் பங்கை எழுத வேண்டும்."],
                 {"type": "callout", "k": "SUBMISSION CHECKLIST",
                  "lines": [("1. Architecture: ", "workflow diagram (6 பெட்டிகள்)"),
                            ("2. Prompts: ", "4 stage prompts (Role+Persona, XML, Few-Shot, JSON)"),
                            ("3. Schema: ", "JSON schema + validation விதிகள்"),
                            ("4. Outputs: ", "3 sample ticket-க்கான JSON + email draft"),
                            ("5. Testing: ", "10 ticket test set + மதிப்பெண் அட்டவணை"),
                            ("6. Report: ", "2 பக்கம் — வடிவமைப்பு, சோதனை, மேம்பாடு")]},
                 bullets=["மதிப்பெண்: accuracy 30, format 20, tone 20, testing 20, documentation 10."],
                 bullets_h=0.42,
                 outcome="ஒரு முழுமையான AI support workflow-ஐ வடிவமைத்து, சோதித்து, ஆவணப்படுத்த முடியும்."))

    out.append(W("ANSWER KEY · ஆசிரியருக்கு", "Answer Key & மதிப்பீட்டு குறிப்பு",
                 ["MCQ விடைகளும், short answer-க்கான எதிர்பார்ப்புகளும் இங்கே.",
                  "Practical பகுதிக்கு rubric அடிப்படையில் மதிப்பிடுங்கள்."],
                 {"type": "table", "rows": [
                     ["பகுதி", "விடை / எதிர்பார்ப்பு"],
                     ["MCQ 1–5", "1-b, 2-b, 3-b, 4-c, 5-a"],
                     ["MCQ 6–10", "6-c, 7-b, 8-c, 9-b, 10-a"],
                     ["Short 1", "Role = நிபுணர் அடையாளம்; Persona = tone + audience"],
                     ["Short 2", "நன்மை: எல்லை தெளிவு, மீள்பயன்; வரம்பு: token செலவு, மூடாத tag"],
                     ["Short 3", "பிரதிநிதித்துவம், சமநிலை, தெளிவான label, ஒரே format"],
                     ["Short 4", "Request → Task analysis → Tool → Observation → Response"],
                     ["Short 5", "{{variable}} இடங்களில் மதிப்பு நிரப்புதல் + உதாரணம்"]],
                  "widths": [0.22, 0.78], "size": 9.8},
                 outcome="மாணவர் விடைகளை நியாயமாக, ஒரே தரத்தில் மதிப்பிட முடியும்."))

    out.append(dict(kind="statement",
                    kicker="CONCLUSION",
                    paras=[("Good AI results start with clear instructions.", dict(size=27, bold=True)),
                           ("Learn to communicate with AI effectively and turn ideas into practical solutions.",
                            dict(size=20))],
                    who="Prompt Engineering · Beginner to Advanced · 14 Modules",
                    notes="இந்த வாக்கியத்தை மாணவர்களைச் சொல்லச் செய்து வகுப்பை முடிக்கவும்."))

    out.append(W("THANK YOU", "நன்றி — அடுத்த படி என்ன?",
                 ["இந்த deck-ஐ மீண்டும் படித்து, ஒவ்வொரு module-ன் practical prompt-ஐயும் இயக்கிப் பாருங்கள்.",
                  "தினமும் ஒரு prompt எழுதினால், ஒரு மாதத்தில் நீங்கள் நிபுணராகிவிடுவீர்கள்."],
                 {"type": "cards", "cols": 3, "max_h": 2.0, "cards": [
                     {"k": "PRACTICE", "t": "Prompt notebook", "s": "ஒவ்வொரு நாளும் ஒரு prompt எழுதி, output-ஐ ஒப்பிடுங்கள்."},
                     {"k": "BUILD", "t": "Mini project", "s": "IT support assistant-ஐ முழுமையாக உருவாக்குங்கள்."},
                     {"k": "SHARE", "t": "Prompt library", "s": "வெற்றி prompt-களைக் குழுவுடன் பகிருங்கள்."}]},
                 outcome="Course நிறைவு — தொடர்ந்து பயிற்சி செய்வதே அடுத்த படி.",
                 notes="மாணவர்களின் சந்தேகங்களுக்கு இடம் கொடுத்து வகுப்பை முடிக்கவும்."))
    return out
