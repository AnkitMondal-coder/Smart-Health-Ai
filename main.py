# backend/main.py


from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
import logging

app = FastAPI()

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (for development only)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Symptom to diagnosis mapping
SYMPTOM_DIAGNOSIS = {
    "headache": ["Tension Headache", "Migraine", "Dehydration"],
    "stomach pain": ["Gastritis", "Food Poisoning", "Appendicitis"],
    "fever": ["Flu", "Viral Infection", "Malaria"],
    "cough": ["Common Cold", "Bronchitis", "COVID-19"],
    "chest pain": ["Heartburn", "Muscle Strain", "Angina"],
    "nausea": ["Food Poisoning", "Pregnancy", "Motion Sickness"],
    "fatigue": ["Anemia", "Hypothyroidism", "Depression"],
    "dizziness": ["Low Blood Pressure", "Vertigo", "Dehydration"],
    "sore throat": ["Common Cold", "Strep Throat", "Tonsillitis"],
    "runny nose": ["Allergic Rhinitis", "Common Cold", "Sinus Infection"],
    "congestion": ["Sinusitis", "Common Cold", "Allergy"],
    "ear pain": ["Ear Infection", "Wax Buildup", "TMJ Disorder"],
    "toothache": ["Cavity", "Gum Infection", "Tooth Sensitivity"],
    "bad breath": ["Gum Disease", "Dry Mouth", "GERD"],
    "itchy skin": ["Eczema", "Allergic Reaction", "Dry Skin"],
    "rash": ["Allergic Dermatitis", "Eczema", "Fungal Infection"],
    "hives": ["Allergic Reaction", "Insect Bite", "Stress"],
    "swollen lymph nodes": ["Infection", "Mononucleosis", "Lymphoma"],
    "back pain": ["Muscle Strain", "Herniated Disc", "Arthritis"],
    "neck pain": ["Muscle Strain", "Cervical Spondylosis", "Whiplash"],
    "shoulder pain": ["Frozen Shoulder", "Rotator Cuff Injury", "Arthritis"],
    "joint pain": ["Arthritis", "Gout", "Injury"],
    "numbness in hands or feet": ["Peripheral Neuropathy", "Diabetes", "Vitamin B12 Deficiency"],
    "cold hands and feet": ["Poor Circulation", "Raynaud's Disease", "Anemia"],
    "night sweats": ["Menopause", "Tuberculosis", "Lymphoma"],
    "weight loss (unexplained)": ["Hyperthyroidism", "Cancer", "Diabetes"],
    "weight gain (unexplained)": ["Hypothyroidism", "PCOS", "Cushing's Syndrome"],
    "shortness of breath": ["Asthma", "Pneumonia", "Heart Failure"],
    "palpitations": ["Anxiety", "Arrhythmia", "Hyperthyroidism"],
    "swollen feet": ["Heart Failure", "Kidney Disease", "Venous Insufficiency"],
    "blurred vision": ["Diabetes", "Glaucoma", "Migraine"],
    "dry eyes": ["Allergy", "Sjogren's Syndrome", "Dehydration"],
    "eye twitching": ["Fatigue", "Magnesium Deficiency", "Stress"],
    "ringing in ears": ["Tinnitus", "Hearing Loss", "Meniere’s Disease"],
    "difficulty swallowing": ["GERD", "Throat Infection", "Esophageal Stricture"],
    "excessive thirst": ["Diabetes", "Dehydration", "Kidney Disease"],
    "frequent urination": ["Diabetes", "Urinary Tract Infection", "Overactive Bladder"],
    "burning sensation during urination": ["UTI", "STI", "Kidney Stones"],
    "dark urine": ["Liver Disease", "Dehydration", "Blood in Urine"],
    "bloating": ["IBS", "Lactose Intolerance", "Gas"],
    "constipation": ["Low Fiber Diet", "Hypothyroidism", "Irritable Bowel Syndrome"],
    "diarrhea": ["Food Poisoning", "IBS", "Infection"],
    "bloody stool": ["Hemorrhoids", "Colorectal Cancer", "Gastrointestinal Bleeding"],
    "rectal pain": ["Hemorrhoids", "Anal Fissure", "Proctitis"],
    "low libido": ["Depression", "Hormonal Imbalance", "Medication Side Effects"],
    "erectile dysfunction": ["Diabetes", "Hypertension", "Psychological Stress"],
    "pain during intercourse": ["Vaginal Dryness", "Infection", "Pelvic Inflammatory Disease"],
    "irregular periods": ["PCOS", "Thyroid Disorder", "Stress"],
    "heavy menstrual bleeding": ["Fibroids", "Hormonal Imbalance", "Blood Clotting Disorder"],
    "painful periods": ["Endometriosis", "Fibroids", "Adenomyosis"],
    "vaginal itching": ["Yeast Infection", "STI", "Allergic Reaction"],
    "vaginal discharge (abnormal)": ["Bacterial Vaginosis", "STI", "Yeast Infection"],
    "breast pain": ["Hormonal Changes", "Cyst", "Mastitis"],
    "lump in breast": ["Fibroadenoma", "Breast Cyst", "Breast Cancer"],
    "hot flashes": ["Menopause", "Hormonal Imbalance", "Anxiety"],
    "weakness": ["Anemia", "Chronic Fatigue Syndrome", "Neurological Disorder"],
    "shaking hands": ["Parkinson’s Disease", "Essential Tremor", "Anxiety"],
    "memory loss": ["Dementia", "Vitamin Deficiency", "Stroke"],
    "hallucinations": ["Schizophrenia", "Dementia", "Drug Intoxication"],
    "difficulty sleeping": ["Insomnia", "Anxiety", "Depression"],
    "excessive sleeping": ["Sleep Apnea", "Narcolepsy", "Depression"],
    "involuntary muscle spasms": ["Dehydration", "Neurological Disorder", "Electrolyte Imbalance"],
    "leg cramps": ["Dehydration", "Magnesium Deficiency", "Varicose Veins"],
    "restless legs": ["Iron Deficiency", "Nerve Disorder", "Pregnancy"]

}

# Remedies mapping
SYMPTOM_REMEDIES = {
    "headache": ["Drink water", "Take rest", "Try mild pain relievers"],
    "stomach pain": ["Avoid spicy food", "Take antacid", "Drink warm water"],
    "fever": ["Stay hydrated", "Rest", "Take paracetamol if needed"],
    "cough": ["Drink warm fluids", "Use cough syrup", "Inhale steam"],
    "chest pain": ["Avoid heavy meals", "Try antacids", "Seek medical help if severe"],
    "nausea": ["Take ginger tea", "Avoid strong smells", "Try deep breathing"],
    "fatigue": ["Improve sleep schedule", "Check for anemia", "Stay active"],
    "dizziness": ["Lie down for a while", "Drink water", "Check blood pressure"],
    "sore throat": ["Gargle with warm salt water", "Drink warm fluids", "Use throat lozenges"],
    "runny nose": ["Use a humidifier", "Drink plenty of fluids", "Take antihistamines if allergies"],
    "congestion": ["Steam inhalation", "Use a saline nasal spray", "Drink warm liquids"],
    "ear pain": ["Apply a warm compress", "Use OTC pain relievers", "Avoid inserting objects in the ear"],
    "toothache": ["Rinse mouth with warm salt water", "Apply a cold compress", "Take pain relievers"],
    "bad breath": ["Maintain oral hygiene", "Stay hydrated", "Chew sugar-free gum"],
    "itchy skin": ["Apply moisturizer", "Use anti-itch creams", "Avoid harsh soaps"],
    "rash": ["Apply calamine lotion", "Avoid scratching", "Use antihistamines if allergic"],
    "hives": ["Apply cold compress", "Take antihistamines", "Avoid known allergens"],
    "swollen lymph nodes": ["Apply warm compress", "Stay hydrated", "Get enough rest"],
    "back pain": ["Use hot or cold packs", "Practice good posture", "Do gentle stretching"],
    "neck pain": ["Apply a warm or cold compress", "Do neck stretches", "Maintain proper posture"],
    "shoulder pain": ["Apply ice or heat", "Do gentle exercises", "Avoid heavy lifting"],
    "joint pain": ["Use a warm compress", "Take OTC pain relievers", "Do low-impact exercises"],
    "numbness in hands or feet": ["Do gentle stretching", "Improve blood circulation", "Take vitamin B12 if deficient"],
    "cold hands and feet": ["Wear warm socks/gloves", "Stay active", "Massage hands and feet"],
    "night sweats": ["Keep room cool", "Wear breathable fabrics", "Stay hydrated"],
    "weight loss (unexplained)": ["Increase calorie intake", "Eat nutrient-rich foods", "Consult a doctor"],
    "weight gain (unexplained)": ["Exercise regularly", "Monitor diet", "Check hormone levels"],
    "shortness of breath": ["Practice deep breathing", "Use a humidifier", "Seek medical help if severe"],
    "palpitations": ["Practice stress reduction techniques", "Avoid caffeine", "Stay hydrated"],
    "swollen feet": ["Elevate legs", "Reduce salt intake", "Stay active"],
    "blurred vision": ["Rest eyes regularly", "Use eye drops", "Consult an eye specialist"],
    "dry eyes": ["Use artificial tears", "Blink frequently", "Limit screen time"],
    "eye twitching": ["Get enough sleep", "Increase magnesium intake", "Reduce stress"],
    "ringing in ears": ["Avoid loud noises", "Reduce caffeine intake", "Manage stress"],
    "difficulty swallowing": ["Eat soft foods", "Drink warm liquids", "Avoid spicy foods"],
    "excessive thirst": ["Drink plenty of water", "Limit caffeine", "Monitor blood sugar levels"],
    "frequent urination": ["Reduce caffeine and alcohol intake", "Do pelvic floor exercises", "Check for infections"],
    "burning sensation during urination": ["Drink cranberry juice", "Stay hydrated", "Avoid spicy foods"],
    "dark urine": ["Drink more water", "Avoid alcohol", "Consult a doctor if persistent"],
    "bloating": ["Avoid carbonated drinks", "Eat slowly", "Try probiotics"],
    "constipation": ["Increase fiber intake", "Stay hydrated", "Exercise regularly"],
    "diarrhea": ["Drink ORS solution", "Eat bananas and rice", "Avoid dairy and fatty foods"],
    "bloody stool": ["Increase fiber intake", "Avoid straining", "Seek medical advice"],
    "rectal pain": ["Use warm sitz baths", "Apply topical creams", "Increase fiber intake"],
    "low libido": ["Reduce stress", "Exercise regularly", "Check for hormonal imbalances"],
    "erectile dysfunction": ["Exercise regularly", "Maintain a healthy diet", "Reduce alcohol consumption"],
    "pain during intercourse": ["Use lubricants", "Practice relaxation techniques", "Consult a doctor if persistent"],
    "irregular periods": ["Maintain a healthy weight", "Manage stress", "Exercise regularly"],
    "heavy menstrual bleeding": ["Use heating pads", "Increase iron intake", "Consult a doctor if excessive"],
    "painful periods": ["Use heating pads", "Take anti-inflammatory pain relievers", "Practice relaxation techniques"],
    "vaginal itching": ["Wear breathable cotton underwear", "Avoid scented products", "Use antifungal creams if needed"],
    "vaginal discharge (abnormal)": ["Maintain good hygiene", "Avoid douching", "Consult a doctor if persistent"],
    "breast pain": ["Wear a supportive bra", "Apply warm compress", "Reduce caffeine intake"],
    "lump in breast": ["Monitor for changes", "Apply warm compress if painful", "Consult a doctor"],
    "hot flashes": ["Wear lightweight clothing", "Avoid caffeine and spicy foods", "Practice deep breathing"],
    "weakness": ["Eat a balanced diet", "Stay hydrated", "Check for vitamin deficiencies"],
    "shaking hands": ["Reduce caffeine intake", "Practice relaxation techniques", "Check for underlying conditions"],
    "memory loss": ["Keep mentally active", "Eat brain-healthy foods", "Manage stress"],
    "hallucinations": ["Reduce stress", "Avoid alcohol and drugs", "Seek medical help"],
    "difficulty sleeping": ["Maintain a bedtime routine", "Limit screen time before bed", "Avoid caffeine before bedtime"],
    "excessive sleeping": ["Stay active during the day", "Regulate sleep schedule", "Consult a doctor if excessive"],
    "involuntary muscle spasms": ["Stay hydrated", "Stretch regularly", "Increase potassium intake"],
    "leg cramps": ["Stretch before bed", "Stay hydrated", "Take magnesium supplements if needed"],
    "restless legs": ["Take warm baths", "Increase iron intake", "Do gentle leg exercises"]
    
}


@app.get("/")
def read_root():
    return {"message": "Smart Health Assistant Backend is Running!"}


@app.post("/analyze-symptoms/")
async def analyze_symptoms_route(request: Request):
    data = await request.json()
    symptom = data.get("symptom")

    if not symptom:
        raise HTTPException(status_code=400, detail="Symptom is required")

    # Process the symptom directly (no voice capture in backend)
    diagnosis, remedies = process_symptoms([symptom])

    return {
        "symptom": symptom,
        "diagnosis": diagnosis,  # Return the list of diagnoses
        "remedies": remedies,  # Return the list of remedies
        #"disclaimer": "This is an AI-based preliminary diagnosis. Please consult a healthcare professional for a final diagnosis."
    }


def process_symptoms(symptoms):
    diagnosis_result = []
    remedy_suggestions = []

    for symptom in symptoms:
        symptom = symptom.lower().strip()
        if symptom in SYMPTOM_DIAGNOSIS:
            possible_conditions = SYMPTOM_DIAGNOSIS[symptom]
            diagnosis_result.append(f"Possible conditions - {', '.join(possible_conditions)}")

            if symptom in SYMPTOM_REMEDIES:
                remedies = SYMPTOM_REMEDIES[symptom]
                remedy_suggestions.append(f"Suggested remedies - {', '.join(remedies)}")
            else:
                remedy_suggestions.append("No remedies found.")
        else:
            diagnosis_result.append("No diagnosis data available.")
            remedy_suggestions.append("No remedies found.")

    return diagnosis_result, remedy_suggestions

