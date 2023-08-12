import string

def get_bot_response(user_message):
    responses = {
    "hallo": "Hallo! Wie kann ich Ihnen helfen?",
    "was ist das MVZ Kehl?": "Das Hausärztliches Medizinisches Versorgungszentrum (MVZ) Kehl ist ein Zusammenschluss der Praxen Dres. Wenger, Renner, von Plehn und Cucuiu. Es bietet moderne hausärztliche Versorgung in Kehl und Umgebung.",
    "wo befinden sich Ihre Standorte?": "Wir haben zwei Standorte: Hauptstr. 107 in Kehl und Am Storchennest 16 in Kehl-Sundheim.",
    "haben Sie während des Urlaubs geöffnet?": "Durch die Verzahnung der drei Standorte haben Sie auch in Urlaubszeiten eine interne Vertretung im gewohnten Team.",
    "was ist eine VERAH?": "VERAH steht für Medizinische Fachangestellte, auch „Arzthelferin“ genannt, die für Hausbesuche ausgebildet wurde.",
    "wann ist der Sommerurlaub 2023?": "Der Sommerurlaub 2023 für die Praxis Sundheim ist vom 22. Juli bis 13. August.",
    "bieten Sie 3D-EKG an?": "Ja, wir bieten 3D-EKG zur frühzeitigen Erkennung der Koronaren Herzkrankheit an.",
    "führen Sie Impfungen durch?": "Ja, wir führen alle Standardimpfungen durch.",
    "welche Leistungen bieten Sie an?": "Wir bieten verschiedene Leistungen an, darunter EKG, Langzeit EKG, Langzeit Blutdruckmessung und Lungenfunktionstests.",
    "haben Sie Stellenangebote?": "Ja, wir haben Stellenangebote. Sie können sich auf unserer Website darüber informieren.",
    "wie kann ich Sie kontaktieren?": "Sie können uns unter der Telefonnummer 07851-2965 oder per E-Mail unter hausaerztlichesMVZKehl@web.de erreichen.",
    "wann haben Sie geöffnet?": "Unsere Öffnungszeiten variieren je nach Standort. Bitte informieren Sie sich auf unserer Website über die genauen Zeiten.",
    "muss ich einen Termin vereinbaren?": "Ja, bitte melden Sie sich immer telefonisch an.",
    "wo befindet sich die Praxis von Plehn?": "Die Praxis von Plehn befindet sich in Am Storchennest 16, 77694 Kehl.",
    "wie kann ich die Praxis von Plehn kontaktieren?": "Sie können die Praxis von Plehn unter der Telefonnummer 07851-2574 oder per E-Mail unter info@praxis-von-plehn.de erreichen.",
    "bieten Sie auch Sprechstunden in Englisch an?": "Ja, wir bieten auch Informationen auf Englisch an.",
    "bieten Sie auch Sprechstunden in Französisch an?": "Ja, wir bieten auch Informationen auf Französisch an.",
    "was ist ein MVZ?": "MVZ steht für Medizinisches Versorgungszentrum.",
    "was bedeutet 'hausärztliche Versorgung'?": "Hausärztliche Versorgung bezieht sich auf die allgemeinmedizinische Betreuung und Behandlung von Patienten.",
    "was ist ein EKG?": "Ein EKG ist ein Elektrokardiogramm, ein Test, der die elektrische Aktivität des Herzens misst.",
    "was ist ein Langzeit EKG?": "Ein Langzeit EKG zeichnet die elektrische Aktivität des Herzens über einen längeren Zeitraum auf, in der Regel 24 Stunden.",
    "was ist eine Lungenfunktion?": "Eine Lungenfunktionstest misst, wie gut Ihre Lungen arbeiten.",
    "wie kann ich einen Termin vereinbaren?": "Bitte rufen Sie uns an, um einen Termin zu vereinbaren.",
    "bieten Sie Hausbesuche an?": "Ja, wir bieten Hausbesuche an. Sprechen Sie uns bei Fragen gerne direkt an.",
    "was ist ein 3D-EKG?": "Ein 3D-EKG ist eine fortschrittliche Methode zur Erkennung der Koronaren Herzkrankheit.",
    "welche Impfungen bieten Sie an?": "Wir führen alle Standardimpfungen durch. Bitte informieren Sie sich auf unserer Website oder kontaktieren Sie uns für weitere Informationen.",
    "wo finde ich Ihre Stellenangebote?": "Unsere Stellenangebote finden Sie auf unserer Website unter dem Menüpunkt 'Stellenangebote'.",
    "haben Sie auch andere Standorte?": "Ja, wir haben einen weiteren Standort am Storchennest 16 in Kehl-Sundheim.",
    "wie kann ich mich bei Ihnen bewerben?": "Bitte informieren Sie sich auf unserer Website über die aktuellen Stellenangebote und den Bewerbungsprozess.",
    "was ist ein Langzeit Blutdruck?": "Ein Langzeit Blutdruck ist eine Messung des Blutdrucks über einen Zeitraum von 24 Stunden.",
    "was ist Sonographie?": "Sonographie ist eine bildgebende Untersuchungsmethode, die mit Ultraschallwellen arbeitet. Wir führen Sonographien von verschiedenen Körperregionen durch, wie z.B. Abdomen, Schilddrüse und Thorax.",
    "was ist Arteriographie?": "Arteriographie ist eine Methode zur Messung des Gefäßalters.",
    "was ist pAVK Screening?": "pAVK Screening mittels ABI-Messung ist eine Untersuchung auf Durchblutungsstörung der Beine.",
    "was ist Check Up Vorsorge Untersuchung?": "Check Up Vorsorge Untersuchung ist eine allgemeine Gesundheitsuntersuchung zur Früherkennung von Krankheiten.",
    "bieten Sie Hautkrebs Screening an?": "Ja, wir bieten Hautkrebs Screening an.",
    "was bedeutet 'Kleine Chirurgie'?": "Kleine Chirurgie bezieht sich auf kleinere chirurgische Eingriffe und Wundbehandlungen, die in der Praxis durchgeführt werden können.",
    "was ist DMP?": "DMP steht für Disease Management Programme. Es handelt sich um Programme der Krankenkassen zur regelmäßigen Betreuung von Patienten mit bestimmten Erkrankungen.",
    "was ist ein EKG Langzeit?": "Ein EKG Langzeit zeichnet die elektrische Aktivität des Herzens über einen längeren Zeitraum, in der Regel 24 Stunden, auf.",
    "was ist Lungenfunktion und Bestimmung der Sauerstoffsättigung?": "Lungenfunktionstests messen, wie gut Ihre Lungen arbeiten. Die Bestimmung der Sauerstoffsättigung gibt an, wie viel Sauerstoff Ihr Blut transportieren kann.",
    "führen Sie Laboruntersuchungen durch?": "Ja, wir führen Labor- und Speziallaboruntersuchungen durch.",
    "was ist ein Schnelltest auf Herzinfarkt?": "Es handelt sich um einen Test, der in der Praxis durchgeführt wird, um schnell festzustellen, ob ein Patient einen Herzinfarkt hat oder eine Lungenembolie vorliegt.",
    "wie kann ich meine Datenfreigabe für die Website ändern?": "Sie können Ihre Datenfreigabeeinstellungen auf unserer Website anpassen. Wählen Sie die gewünschte Datenzugriffsebene und -dauer aus.",
    
    }

    responses = {k.lower(): v for k, v in responses.items()}


     # Convert user message to lowercase and strip
    user_message = user_message.lower().strip()

    # Get the response from the dictionary, if it exists
    return responses.get(user_message, "Es tut mir leid, aber ich habe die Frage nicht verstanden.")


