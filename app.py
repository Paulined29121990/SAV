import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Service Client Kassel", layout="centered")


# --- Largeur personnalisée ---
st.markdown("""
<style>
.main {
    max-width: 1100px;
    margin: auto;
}
</style>
""", unsafe_allow_html=True)


# --- CSS GLOBAL ---
st.markdown("""
<style>
body {
    background-color: #ffffff;
    font-family: 'Georgia', serif;
}
.title {
    text-align: center;
    font-size: 42px;
    color: #000;
    margin-top: 20px;
}
.subtitle {
    text-align: center;
    font-size: 14px;
    color: #555;
    letter-spacing: 2px;
    margin-bottom: 40px;
}
</style>
""", unsafe_allow_html=True)


def reset_app():
    for key in list(st.session_state.keys()):
        del st.session_state[key]
    st.rerun()

# --- Logo ---
col1, col2, col3 = st.columns([1,0.5,1])
with col2:
    st.image("assets/logo_diamond.jpg", width=120)

# --- Titre ---
st.markdown('<div class="title">Service Client Kassel</div>', unsafe_allow_html=True)


# Initialiser la langue si pas encore choisie
if "langue_choisie" not in st.session_state:
    st.session_state["langue_choisie"] = None

# Si pas encore choisi → afficher le sélecteur
if st.session_state["langue_choisie"] is None:

    st.markdown(
        '<div class="subtitle">SELECT YOUR LANGUAGE · CHOISISSEZ VOTRE LANGUE · SELECCIONE SU IDIOMA</div>',
        unsafe_allow_html=True
    )

    langue = st.selectbox(
        "",
        ["Français", "English", "Español", "Deutsch"],
        index=None,
        placeholder="Choisissez votre langue"
    )

    if langue:
        st.session_state["langue_choisie"] = langue
        st.rerun()

    st.stop()  # ⛔ arrête l’exécution tant que la langue n’est pas choisie

# --- À partir d’ici : langue choisie ---
langue = st.session_state["langue_choisie"]

lang_code = {
    "Français": "fr",
    "English": "en",
    "Español": "es",
    "Deutsch": "de"
}[langue]


# Bouton retour à la sélection de langue (style élégant)
st.markdown("""
<div style="text-align:left; margin-top:10px;">
    <form action="" method="get">
        <button style="
            background:none;
            border:none;
            color:#b5983a;
            font-size:16px;
            cursor:pointer;
        ">← Changer de langue</button>
        <input type="hidden" name="retour" value="1">
    </form>
</div>
""", unsafe_allow_html=True)

# Vérifier la présence du paramètre "retour" dans l'URL
params = st.query_params

if "retour" in params:
    st.query_params.clear()
    reset_app()




liens_certificat = {
    "AMAZONIA": "https://www.amazonia-bijoux.fr/content/6-garantie",
    "ANDREA BELLINI": "https://www.andrea-bellini.com/content/7-garantie",
    "ATELIER DU DIAMANT": "https://www.atelier-diamant.fr/",
    "BY COLETTE": "https://www.bycolette-bijoux.fr/",
    "CARATELLI": "https://www.caratelli-gioielli.com/content/6-garantie",
    "DI JOYA": "https://www.dijoya.fr/content/7-garantie",
    "COMPTOIR DU DIAMANT": "https://www.comptoir-diamant.fr/content/6-garantie",
    "CREA EN OR": "https://www.crea-en-or.com/",
    "DIAMANTA": "https://www.diamanta.fr/content/10-garantie",
    "DIAMOND AND CO": "https://www.diamondandco.fr/content/10-garantie",
    "LA MAISON DE LA JOAILLERIE": "https://maisonjoaillerie.com/content/7-garantie",
    "L'ARTISAN JOALLIER": "https://www.lartisan-joaillier.fr/content/6-garantie",
    "LE DIAMANTAIRE": "https://www.le-diamantaire.fr/index.php?id_lang=1",
    "L'EXCEPTION": "https://lexception-bijoux.fr/index.php?id_cms=6&controller=cms",
    "L'INSTANT D'OR": "https://www.linstant-dor.com/content/6-garantie",
    "MAISON HERITAGE": "https://www.joaillerie-maisonheritage.com/content/6-garantie",
    "MUSE": "https://www.muse-jewels.fr/",
    "OR BY DIAMANTA": "https://www.lor-by-diamanta.fr/content/8-plateforme-garantie",
    "OR ECLAT": "https://www.oreclat.fr/content/6-garantie",
    "ORO DI ORO": "https://www.orodioro.fr/content/10-ma-garantie",
    "PARIS JOAILLERIE": "https://www.parisjoaillerie.com/content/6-garantie",
    "PARIS VENDOME": "https://parisvendome-joaillerie.fr/30-joaillerie",
    
}

st.session_state["langue"] = lang_code

# Toujours initialiser les variables boutons
btn_mise_taille = False
btn_demande_retour = False
st.session_state.setdefault("procedure", None)


# ------------------------------
# INTERFACE SELON LA LANGUE
# ------------------------------

if st.session_state["langue"] == "fr":
    st.markdown("")
    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("Mise à taille", key="fr_option1"):
            st.session_state["procedure"] = "mise_taille"


    with col2:
        if st.button("Demande de réparation", key="fr_option2"):
            st.session_state["procedure"] = "retour"
        
    with col3:
        if st.button("Besoin de certificat", key="fr_option3"):
            st.session_state["procedure"] = "certificat_fr"





elif st.session_state["langue"] == "en":
    st.markdown("")
    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("Resizing", key="en_option1"):
            st.session_state["procedure"] = "resize_en"

    with col2:
        if st.button("Repair request", key="en_option2"):
            st.session_state["procedure"] = "return_en"

    with col3:
        if st.button("Certificate", key="en_option3"):
            st.session_state["procedure"] = "certificat_en"


elif st.session_state["langue"] == "es":
    st.markdown("### ¿Qué desea hacer?")
    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("Ajuste de tamaño", key="es_option1"):
            st.session_state["procedure"] = "resize_es"

    with col2:
        if st.button("Solicitud de reparación", key="es_option2"):
            st.session_state["procedure"] = "return_es"

    with col3:
        if st.button("Certificado", key="es_option3"):
            st.session_state["procedure"] = "certificat_es"





elif st.session_state["langue"] == "de":
    st.markdown("")
    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("Größenanpassung", key="de_option1"):
            st.session_state["procedure"] = "resize_de"

    with col2:
        if st.button("Reparaturanfrage", key="de_option2"):
            st.session_state["procedure"] = "return_de"

    with col3:
        if st.button("Zertifikat", key="de_option3"):
            st.session_state["procedure"] = "certificat_de"



# ------------------------------
# STYLE DES BOUTONS
# ------------------------------
st.markdown("""
<style>
button[kind="secondary"] {
    background-color: #fafafa !important;
    border: 2px solid #b5983a !important;
    border-radius: 12px !important;
    padding: 25px !important;
    width: 170px !important;
    height: 90px !important;
    font-size: 20px !important;
}
</style>
""", unsafe_allow_html=True)


# ------------------------------
# LOGIQUE : MISE À TAILLE
# ------------------------------
if st.session_state.get("langue") == "fr":
    if st.session_state.get("show_mise_taille") is None:
        st.session_state["show_mise_taille"] = False
        

    if 'btn_mise_taille' in locals() and btn_mise_taille:
        st.session_state["show_mise_taille"] = True

    if btn_demande_retour:
        st.session_state["show_retour"] = True



if st.session_state["procedure"] == "mise_taille":


    html_block = """
    <style>
    .lux-box {
        border: 1.5px solid #d7c27a;
        border-radius: 12px;
        padding: 28px;
        background: linear-gradient(145deg, #fbfbf9, #ffffff);
        box-shadow: 0 4px 18px rgba(0,0,0,0.08);
        margin-top: 30px;
        margin-bottom: 20px;
        font-family: Georgia, serif;
    }

    .lux-title {
        font-size: 24px;
        font-weight: 700;
        color: #b5983a;
        text-align: center;
        margin-bottom: 12px;
        letter-spacing: 1px;
    }

    .lux-subtitle {
        text-align: center;
        font-size: 14px;
        color: #6e6e6e;
        margin-bottom: 20px;
    }

    .lux-text {
        font-size: 17px;
        color: #444;
        line-height: 1.7;
    }

    .lux-text strong {
        color: #b5983a;
    }

    .lux-link {
        color: #b5983a;
        font-weight: 600;
        text-decoration: none;
    }

    .lux-link:hover {
        text-decoration: underline;
    }
    </style>

    <div class="lux-box">
        <div class="lux-title">💍 Mise à Taille</div>
        <div class="lux-subtitle">Informations importantes concernant votre bijou</div>

        <div class="lux-text">
            Vous pouvez bénéficier d’une <strong>mise à taille offerte</strong>  
            (bague neuve, non portée, or et diamants uniquement)  
            sur une tolérance de <strong>± deux tailles</strong> durant la période de garantie.<br><br>

            Au-delà de 2 tailles ou si la mise à taille n’était pas proposée (pour votre modèle ou lors de la vente) 
            un montant de <strong>60€</strong> vous sera demandé pour une nouvelle fabrication.<br><br>

            Les modèles en <strong>zirconium</strong> ne bénéficient pas du service offert.  
            Un devis <strong>forfaitaire de 50€</strong> sera automatiquement appliqué.<br><br>

            📄 Formulaire de retour :  
            <a class="lux-link" href="https://www.kassel.fr/service-apres-vente/bijoux/bijoux-or.html" target="_blank">
                Cliquez ici pour accéder au formulaire
            </a><br><br>

            ⏳ Délais atelier :  
            le traitement nécessite <strong>6 à 8 semaines</strong> à compter de la réception du bijou.<br><br>

            📦 Adresse d’envoi :  
            merci d’envoyer votre colis exclusivement à  
            <strong>PINACLE 100</strong>  
            (tout envoi ailleurs sera refusé).<br><br>

            
        </div>
    </div>
    """

    components.html(html_block, height=750, scrolling=True)




if st.session_state["procedure"] == "retour":

    html_retour = """
    <style>
    .lux-box {
        border: 1.5px solid #d7c27a;
        border-radius: 12px;
        padding: 28px;
        background: linear-gradient(145deg, #fbfbf9, #ffffff);
        box-shadow: 0 4px 18px rgba(0,0,0,0.08);
        margin-top: 30px;
        margin-bottom: 20px;
        font-family: Georgia, serif;
    }

    .lux-title {
        font-size: 24px;
        font-weight: 700;
        color: #b5983a;
        text-align: center;
        margin-bottom: 12px;
        letter-spacing: 1px;
    }

    .lux-subtitle {
        text-align: center;
        font-size: 14px;
        color: #6e6e6e;
        margin-bottom: 20px;
    }

    .lux-text {
        font-size: 17px;
        color: #444;
        line-height: 1.7;
    }

    .lux-text strong {
        color: #b5983a;
    }

    .lux-link {
        color: #b5983a;
        font-weight: 600;
        text-decoration: none;
    }

    .lux-link:hover {
        text-decoration: underline;
    }
    </style>

    <div class="lux-box">
        <div class="lux-title">📦 Demande de Réparation</div>
        <div class="lux-subtitle">Procédure de prise en charge</div>

        <div class="lux-text">

            Bonjour,<br><br>

            Nous sommes désolés d’apprendre que votre bijou nécessite une intervention.<br><br>

            La situation que vous évoquez semble indiquer qu’une prise en charge par notre  
            service client <strong>KASSEL</strong> est nécessaire.<br><br>

            Nous vous invitons à remplir le formulaire de retour disponible sur notre site :<br>
            <a class="lux-link" href="https://www.kassel.fr/service-apres-vente/bijoux/bijoux-or.html" target="_blank">
                Cliquez ici pour accéder au formulaire
            </a><br><br>

            La prise en charge sera effectuée pendant la période de garantie,  
            à condition que votre bijou n’ait subi ni dommage accidentel  
            ni intervention par une personne non agréée par la marque.<br><br>

            ⚠️ La perte et le vol ne sont pas couverts par la garantie.  
            Pour ces situations, nous vous recommandons de contacter votre assurance.<br><br>

            Rappel : notre atelier de réparation ne procède pas aux remboursements.<br><br>

            📦 <strong>Adresse d’envoi obligatoire :</strong><br>
            PINACLE 100<br>
            Tout colis envoyé à une autre adresse sera automatiquement refusé.<br><br>

        </div>
    </div>
    """

    components.html(html_retour, height=900, scrolling=True)




if st.session_state["procedure"] == "resize_en":

    html_resize_en = """
    <style>
    .lux-box {
        border: 1.5px solid #d7c27a;
        border-radius: 12px;
        padding: 28px;
        background: linear-gradient(145deg, #fbfbf9, #ffffff);
        box-shadow: 0 4px 18px rgba(0,0,0,0.08);
        margin-top: 30px;
        margin-bottom: 20px;
        font-family: Georgia, serif;
    }
    .lux-title {
        font-size: 24px;
        font-weight: 700;
        color: #b5983a;
        text-align: center;
        margin-bottom: 12px;
        letter-spacing: 1px;
    }
    .lux-subtitle {
        text-align: center;
        font-size: 14px;
        color: #6e6e6e;
        margin-bottom: 20px;
    }
    .lux-text {
        font-size: 17px;
        color: #444;
        line-height: 1.7;
    }
    .lux-text strong {
        color: #b5983a;
    }
    .lux-link {
        color: #b5983a;
        font-weight: 600;
        text-decoration: none;
    }
    .lux-link:hover {
        text-decoration: underline;
    }
    </style>

    <div class="lux-box">
        <div class="lux-title">💍 Ring Resizing</div>
        <div class="lux-subtitle">Important information about your jewelry</div>

        <div class="lux-text">

            You may benefit from a <strong>free resizing service</strong>  
            (new, unworn rings in gold and diamonds only),  
            within a tolerance of <strong>± two sizes</strong> during the warranty period.<br><br>

            Beyond this limit, or when resizing was not available  
            for your model at the time of purchase,  
            a <strong>€60 fee</strong> will be required for a new fabrication.<br><br>

            ⚠️ Rings made of <strong>zirconium</strong> are not eligible for the free resizing service.  
            A fixed <strong>€50 estimate</strong> will automatically apply.<br><br>

            📄 Return form:  
            <a class="lux-link" href="https://form.typeform.com/to/c7QAwaNU?typeform-source=kassel.typeform.com" target="_blank">
                Click here to access the form
            </a><br><br>

            ⏳ Processing time:  
            <strong>6 to 8 weeks</strong> from reception at our workshop.<br><br>

            📦 Shipping address:  
            Please send your parcel exclusively to  
            <strong>PINACLE 100</strong>.  
            Shipments to any other address will be refused.<br><br>

        
        </div>
    </div>
    """

    components.html(html_resize_en, height=850, scrolling=True)



if st.session_state["procedure"] == "return_en":

    html_return_en = """
    <style>
    .lux-box {
        border: 1.5px solid #d7c27a;
        border-radius: 12px;
        padding: 28px;
        background: linear-gradient(145deg, #fbfbf9, #ffffff);
        box-shadow: 0 4px 18px rgba(0,0,0,0.08);
        margin-top: 30px;
        margin-bottom: 20px;
        font-family: Georgia, serif;
    }
    .lux-title {
        font-size: 24px;
        font-weight: 700;
        color: #b5983a;
        text-align: center;
        margin-bottom: 12px;
        letter-spacing: 1px;
    }
    .lux-subtitle {
        text-align: center;
        font-size: 14px;
        color: #6e6e6e;
        margin-bottom: 20px;
    }
    .lux-text {
        font-size: 17px;
        color: #444;
        line-height: 1.7;
    }
    .lux-text strong {
        color: #b5983a;
    }
    .lux-link {
        color: #b5983a;
        font-weight: 600;
        text-decoration: none;
    }
    .lux-link:hover {
        text-decoration: underline;
    }
    </style>

    <div class="lux-box">
        <div class="lux-title">📦 Return Request</div>
        <div class="lux-subtitle">Return procedure</div>

        <div class="lux-text">

            We are sorry to hear that your jewelry requires a service intervention.<br><br>

            Based on the situation you describe,  
            a verification by our <strong>KASSEL customer service</strong> appears necessary.<br><br>

            Please fill out our return form on the website:<br>
            <a class="lux-link" href="https://form.typeform.com/to/c7QAwaNU?typeform-source=kassel.typeform.com" target="_blank">
                Click here to access the form
            </a><br><br>

            Repairs are covered under warranty only if  
            the jewelry has not suffered accidental damage  
            and has **not** been altered by a non-approved jeweler.<br><br>

            ⚠️ Loss and theft are not covered by the warranty.  
            Please contact your insurance company in such cases.<br><br>

            Reminder: our repair workshop does <strong>not issue refunds</strong>.<br><br>

            📦 <strong>Mandatory shipping address:</strong><br>
            PINACLE 100<br>
            Any parcel sent to another address will be refused.<br><br>

            
        </div>
    </div>
    """

    components.html(html_return_en, height=950, scrolling=True)



if st.session_state["procedure"] == "resize_es":

    html_resize_es = """
    <style>
    .lux-box {border:1.5px solid #d7c27a;border-radius:12px;padding:28px;background:linear-gradient(145deg,#fbfbf9,#ffffff);box-shadow:0 4px 18px rgba(0,0,0,0.08);margin-top:30px;margin-bottom:20px;font-family:Georgia, serif;}
    .lux-title {font-size:24px;font-weight:700;color:#b5983a;text-align:center;margin-bottom:12px;}
    .lux-subtitle {text-align:center;font-size:14px;color:#6e6e6e;margin-bottom:20px;}
    .lux-text {font-size:17px;color:#444;line-height:1.7;}
    .lux-text strong {color:#b5983a;}
    .lux-link {color:#b5983a;font-weight:600;text-decoration:none;}
    .lux-link:hover {text-decoration:underline;}
    </style>

    <div class="lux-box">
        <div class="lux-title">💍 Ajuste de Tamaño</div>
        <div class="lux-subtitle">Información importante sobre su joya</div>

        <div class="lux-text">

            Puede beneficiarse de un <strong>ajuste de tamaño gratuito</strong>  
            (anillos nuevos, sin usar, de oro y diamantes),  
            dentro de una tolerancia de <strong>± dos tallas</strong> durante el período de garantía.<br><br>

            Si su modelo no permite el ajuste o supera ese límite,  
            será necesario un <strong>coste de 60€</strong> para una nueva fabricación.<br><br>

            ⚠️ Los modelos de <strong>circonio</strong> no incluyen este servicio gratuito.  
            Se aplicará automáticamente un <strong>presupuesto fijo de 50€</strong>.<br><br>

            📄 Formulario de devolución:<br>
            <a class="lux-link" href="https://form.typeform.com/to/dzxwzbLD?typeform-source=kassel.typeform.com" target="_blank">
                Haga clic aquí para acceder al formulario
            </a><br><br>

            ⏳ Tiempo de procesamiento:  
            <strong>6 a 8 semanas</strong> desde la recepción en nuestro taller.<br><br>

            📦 Dirección de envío obligatoria:<br>
            <strong>PINACLE 100</strong><br>
            Los envíos a otra dirección serán rechazados.<br><br>

            Quedamos a su disposición para cualquier consulta adicional.
        </div>
    </div>
    """

    components.html(html_resize_es, height=900, scrolling=True)


if st.session_state["procedure"] == "return_es":

    html_return_es = """
    <style>
    .lux-box {border:1.5px solid #d7c27a;border-radius:12px;padding:28px;background:linear-gradient(145deg,#fbfbf9,#ffffff);box-shadow:0 4px 18px rgba(0,0,0,0.08);margin-top:30px;margin-bottom:20px;font-family:Georgia, serif;}
    .lux-title {font-size:24px;font-weight:700;color:#b5983a;text-align:center;margin-bottom:12px;}
    .lux-subtitle {text-align:center;font-size:14px;color:#6e6e6e;margin-bottom:20px;}
    .lux-text {font-size:17px;color:#444;line-height:1.7;}
    .lux-text strong {color:#b5983a;}
    .lux-link {color:#b5983a;font-weight:600;text-decoration:none;}
    .lux-link:hover {text-decoration:underline;}
    </style>

    <div class="lux-box">
        <div class="lux-title">📦 Solicitud de Devolución</div>
        <div class="lux-subtitle">Procedimiento de devolución</div>

        <div class="lux-text">

            Lamentamos que su joya necesite una intervención.<br><br>

            Según lo que describe,  
            es necesaria una verificación por parte de nuestro  
            <strong>Servicio de Atención al Cliente KASSEL</strong>.<br><br>

            Le invitamos a completar el formulario de devolución disponible en nuestra página web:<br>
            <a class="lux-link" href="https://form.typeform.com/to/dzxwzbLD?typeform-source=kassel.typeform.com" target="_blank">
                Haga clic aquí para acceder al formulario
            </a><br><br>

            La garantía cubre la reparación únicamente si la joya  
            <strong>no ha sufrido daños accidentales</strong>  
            y <strong>no ha sido manipulada por terceros no autorizados</strong>.<br><br>

            ⚠️ La pérdida y el robo no están cubiertos por la garantía.  
            Le recomendamos contactar con su seguro en estos casos.<br><br>

            Recordatorio: nuestro taller <strong>no realiza reembolsos</strong>.<br><br>

            📦 <strong>Dirección de envío obligatoria:</strong><br>
            PINACLE 100<br>
            Cualquier envío a otra dirección será rechazado.<br><br>

            Quedamos a su disposición para cualquier consulta adicional.
        </div>
    </div>
    """

    components.html(html_return_es, height=950, scrolling=True)



if st.session_state["procedure"] == "resize_de":

    html_resize_de = """
    <style>
    .lux-box {border:1.5px solid #d7c27a;border-radius:12px;padding:28px;background:linear-gradient(145deg,#fbfbf9,#ffffff);box-shadow:0 4px 18px rgba(0,0,0,0.08);margin-top:30px;margin-bottom:20px;font-family:Georgia, serif;}
    .lux-title {font-size:24px;font-weight:700;color:#b5983a;text-align:center;margin-bottom:12px;}
    .lux-subtitle {text-align:center;font-size:14px;color:#6e6e6e;margin-bottom:20px;}
    .lux-text {font-size:17px;color:#444;line-height:1.7;}
    .lux-text strong {color:#b5983a;}
    .lux-link {color:#b5983a;font-weight:600;text-decoration:none;}
    .lux-link:hover {text-decoration:underline;}
    </style>

    <div class="lux-box">
        <div class="lux-title">💍 Größenanpassung</div>
        <div class="lux-subtitle">Wichtige Informationen zu Ihrem Schmuckstück</div>

        <div class="lux-text">

            Sie können eine <strong>kostenlose Größenanpassung</strong> erhalten  
            (nur für neue, ungetragene Ringe aus Gold und Diamanten),  
            innerhalb einer Toleranz von <strong>± zwei Größen</strong> während der Garantiezeit.<br><br>

            Wenn Ihr Modell dies nicht zulässt oder der Umfang überschritten wird,  
            fällt eine <strong>Gebühr von 60€</strong> für eine Neuanfertigung an.<br><br>

            ⚠️ <strong>Zirkonium-Ringe</strong> sind von diesem kostenlosen Service ausgeschlossen.  
            Ein <strong>Fixpreis von 50€</strong> wird automatisch berechnet.<br><br>

            📄 Rücksendeformular:<br>
            <a class="lux-link" href="https://form.typeform.com/to/igbHcfzE?typeform-source=kassel.typeform.com" target="_blank">
                Hier klicken, um zum Formular zu gelangen
            </a><br><br>

            ⏳ Bearbeitungszeit:  
            <strong>6 bis 8 Wochen</strong> ab Eingang im Atelier.<br><br>

            📦 Versandadresse:  
            Bitte senden Sie Ihr Paket ausschließlich an  
            <strong>PINACLE 100</strong>.  
            Sendungen an andere Adressen werden abgelehnt.<br><br>

            Wir stehen Ihnen gerne für weitere Fragen zur Verfügung.
        </div>
    </div>
    """

    components.html(html_resize_de, height=900, scrolling=True)


if st.session_state["procedure"] == "return_de":

    html_return_de = """
    <style>
    .lux-box {border:1.5px solid #d7c27a;border-radius:12px;padding:28px;background:linear-gradient(145deg,#fbfbf9,#ffffff);box-shadow:0 4px 18px rgba(0,0,0,0.08);margin-top:30px;margin-bottom:20px;font-family:Georgia, serif;}
    .lux-title {font-size:24px;font-weight:700;color:#b5983a;text-align:center;margin-bottom:12px;}
    .lux-subtitle {text-align:center;font-size:14px;color:#6e6e6e;margin-bottom:20px;}
    .lux-text {font-size:17px;color:#444;line-height:1.7;}
    .lux-text strong {color:#b5983a;}
    .lux-link {color:#b5983a;font-weight:600;text-decoration:none;}
    .lux-link:hover {text-decoration:underline;}
    </style>

    <div class="lux-box">
        <div class="lux-title">📦 Rücksendung</div>
        <div class="lux-subtitle">Ablauf der Rücksendung</div>

        <div class="lux-text">

            Es tut uns leid zu hören, dass Ihr Schmuckstück eine Reparatur benötigt.<br><br>

            Aufgrund Ihrer Beschreibung ist eine Überprüfung durch unseren  
            <strong>KASSEL Kundendienst</strong> erforderlich.<br><br>

            Bitte füllen Sie das Rücksendeformular auf unserer Website aus:<br>
            <a class="lux-link" href="https://form.typeform.com/to/igbHcfzE?typeform-source=kassel.typeform.com" target="_blank">
                Hier zum Formular
            </a><br><br>

            Die Garantie deckt Reparaturen nur ab, wenn der Schmuck  
            <strong>keine Unfallschäden</strong> aufweist  
            und <strong>nicht von Dritten verändert</strong> wurde.<br><br>

            ⚠️ Verlust und Diebstahl sind nicht durch die Garantie abgedeckt.  
            Bitte wenden Sie sich an Ihre Versicherung.<br><br>

            Hinweis: unser Reparaturatelier <strong>erstattet keine Rückzahlungen</strong>.<br><br>

            📦 <strong>Verpflichtende Versandadresse:</strong><br>
            PINACLE 100<br>
            Sendungen an andere Adressen werden abgelehnt.<br><br>

            Wir stehen Ihnen gerne zur Verfügung.
        </div>
    </div>
    """

    components.html(html_return_de, height=950, scrolling=True)


if st.session_state["procedure"] == "certificat_fr":

    marques = list(liens_certificat.keys())

    choix = st.selectbox(
        "Choisissez la marque :",
        marques,
        key="certif_fr"
    )

    lien = liens_certificat.get(choix)

    html_certificat = f"""
    <style>
    .lux-box {{
        border: 1.5px solid #d7c27a;
        border-radius: 12px;
        padding: 28px;
        background: linear-gradient(145deg, #fbfbf9, #ffffff);
        box-shadow: 0 4px 18px rgba(0,0,0,0.08);
        margin-top: 30px;
        margin-bottom: 20px;
        font-family: Georgia, serif;
    }}
    .lux-title {{
        font-size: 24px;
        font-weight: 700;
        color: #b5983a;
        text-align: center;
        margin-bottom: 12px;
    }}
    .lux-text {{
        font-size: 17px;
        color: #444;
        line-height: 1.7;
    }}
    .lux-text strong {{
        color: #b5983a;
    }}
    .lux-link {{
        color: #b5983a;
        font-weight: 600;
        text-decoration: none;
    }}
    .lux-link:hover {{
        text-decoration: underline;
    }}
    </style>

    <div class="lux-box">
        <div class="lux-title">📄 Certificat d'authenticité — {choix}</div>

        <div class="lux-text">
            Pour obtenir votre certificat d’authenticité,  
            veuillez vous connecter sur le site de la marque,  
            puis cliquer sur <strong>GARANTIE</strong>.<br><br>

            🔗 Lien direct :  
            <a class="lux-link" href="{lien}" target="_blank">{lien}</a><br><br>

            Vous devrez renseigner certains champs (nom ou référence du bijou,  
            date d’achat, etc.).<br><br>

            📧 Vous recevrez ensuite votre certificat d’authenticité directement par email.
        </div>
    </div>
    """

    components.html(html_certificat, height=550, scrolling=True)

 

if st.session_state["procedure"] == "certificat_en":

    marques = list(liens_certificat.keys())

    choix = st.selectbox(
        "Select the jewelry brand:",
        marques,
        key="certif_en"
    )

    lien = liens_certificat.get(choix)

    html_certificat_en = f"""
    <style>
    .lux-box {{
        border: 1.5px solid #d7c27a;
        border-radius: 12px;
        padding: 28px;
        background: linear-gradient(145deg, #fbfbf9, #ffffff);
        box-shadow: 0 4px 18px rgba(0,0,0,0.08);
        margin-top: 30px;
        margin-bottom: 20px;
        font-family: Georgia, serif;
    }}
    .lux-title {{
        font-size: 24px;
        font-weight: 700;
        color: #b5983a;
        text-align: center;
        margin-bottom: 12px;
    }}
    .lux-text {{
        font-size: 17px;
        color: #444;
        line-height: 1.7;
    }}
    .lux-text strong {{
        color: #b5983a;
    }}
    .lux-link {{
        color: #b5983a;
        font-weight: 600;
        text-decoration: none;
    }}
    .lux-link:hover {{
        text-decoration: underline;
    }}
    </style>

    <div class="lux-box">
        <div class="lux-title">📄 Certificate of Authenticity — {choix}</div>

        <div class="lux-text">
            To obtain your certificate of authenticity,  
            please visit the official brand website  
            and click on <strong>WARRANTY</strong>.<br><br>

            🔗 Direct link:  
            <a class="lux-link" href="{lien}" target="_blank">{lien}</a><br><br>

            You will be asked to provide some information  
            (jewelry name/reference, purchase date, etc.).<br><br>

            📧 You will then receive your certificate by email.
        </div>
    </div>
    """

    components.html(html_certificat_en, height=550, scrolling=True)



if st.session_state["procedure"] == "certificat_es":

    marcas = list(liens_certificat.keys())

    eleccion = st.selectbox(
        "Seleccione la marca de su joya:",
        marcas,
        key="certif_es"
    )

    enlace = liens_certificat.get(eleccion)

    html_certificat_es = f"""
    <style>
    .lux-box {{
        border: 1.5px solid #d7c27a;
        border-radius: 12px;
        padding: 28px;
        background: linear-gradient(145deg, #fbfbf9, #ffffff);
        box-shadow: 0 4px 18px rgba(0,0,0,0.08);
        margin-top: 30px;
        margin-bottom: 20px;
        font-family: Georgia, serif;
    }}
    .lux-title {{
        font-size: 24px;
        font-weight: 700;
        color: #b5983a;
        text-align: center;
        margin-bottom: 12px;
    }}
    .lux-text {{
        font-size: 17px;
        color: #444;
        line-height: 1.7;
    }}
    .lux-text strong {{
        color: #b5983a;
    }}
    .lux-link {{
        color: #b5983a;
        font-weight: 600;
        text-decoration: none;
    }}
    .lux-link:hover {{
        text-decoration: underline;
    }}
    </style>

    <div class="lux-box">
        <div class="lux-title">📄 Certificado de Autenticidad — {eleccion}</div>

        <div class="lux-text">
            Para obtener su certificado de autenticidad,  
            acceda a la página web oficial de la marca  
            y haga clic en <strong>GARANTÍA</strong>.<br><br>

            🔗 Enlace directo:  
            <a class="lux-link" href="{enlace}" target="_blank">{enlace}</a><br><br>

            Se le pedirá completar ciertos datos  
            (nombre o referencia de la joya, fecha de compra, etc.).<br><br>

            📧 Posteriormente recibirá su certificado por correo electrónico.
        </div>
    </div>
    """

    components.html(html_certificat_es, height=550, scrolling=True)



if st.session_state["procedure"] == "certificat_de":

    marken = list(liens_certificat.keys())

    wahl = st.selectbox(
        "Wählen Sie die Schmuckmarke:",
        marken,
        key="certif_de"
    )

    link = liens_certificat.get(wahl)

    html_certificat_de = f"""
    <style>
    .lux-box {{
        border: 1.5px solid #d7c27a;
        border-radius: 12px;
        padding: 28px;
        background: linear-gradient(145deg, #fbfbf9, #ffffff);
        box-shadow: 0 4px 18px rgba(0,0,0,0.08);
        margin-top: 30px;
        margin-bottom: 20px;
        font-family: Georgia, serif;
    }}
    .lux-title {{
        font-size: 24px;
        font-weight: 700;
        color: #b5983a;
        text-align: center;
        margin-bottom: 12px;
    }}
    .lux-text {{
        font-size: 17px;
        color: #444;
        line-height: 1.7;
    }}
    .lux-text strong {{
        color: #b5983a;
    }}
    .lux-link {{
        color: #b5983a;
        font-weight: 600;
        text-decoration: none;
    }}
    .lux-link:hover {{
        text-decoration: underline;
    }}
    </style>

    <div class="lux-box">
        <div class="lux-title">📄 Echtheitszertifikat — {wahl}</div>

        <div class="lux-text">
            Um Ihr Echtheitszertifikat zu erhalten,  
            besuchen Sie bitte die offizielle Website der Marke  
            und klicken Sie auf <strong>GARANTIE</strong>.<br><br>

            🔗 Direkter Link:  
            <a class="lux-link" href="{link}" target="_blank">{link}</a><br><br>

            Sie müssen einige Angaben machen  
            (Schmuckname/Referenz, Kaufdatum usw.).<br><br>

            📧 Anschließend erhalten Sie Ihr Zertifikat per E-Mail.
        </div>
    </div>
    """

    components.html(html_certificat_de, height=550, scrolling=True)