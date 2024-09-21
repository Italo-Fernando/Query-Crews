import streamlit as st

from datetime import datetime

def card_component(title, description, logo_url, logo_caption, background_image, unique_id):
    # Parse the timestamp and format it
    timestamp = datetime.strptime(str(logo_caption), "%Y-%m-%d %H:%M:%S")
    import locale
    locale.setlocale(locale.LC_TIME, 'pt_BR')
    
    formatted_caption = timestamp.strftime("%A - %d/%m").capitalize()
    formatted_caption_hour = timestamp.strftime("%H:%M")
    description = description[:200] + '...' if len(description) > 200 else description

    st.markdown(f"""
    <style>
    .card-{unique_id} {{
        position: relative;
        background-color: #000;
        border-radius: 10px;
        margin: 10px;
        color: white;
        font-family: Arial, sans-serif;
        display: inline-block;
        width: 550px;
        height: 300px;
        overflow: hidden;
    }}

    .movie-bg-{unique_id} {{
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: url('{background_image}?id={unique_id}') center/cover; /* Adicionando um ID único à URL da imagem */
        opacity: 0.4;
        z-index: 1;
    }}

    .chanel-logo-{unique_id} {{
        position: relative;
        display: flex;
        align-items: center;
        height: 100px;
        left: 20px;
        z-index: 3;
    }}

    .chanel-logo-{unique_id} img {{
        border-radius: 50px;
        width: 50px;
        height: 50px;
        object-fit: cover;
    }}

    .chanel-logo-{unique_id} figcaption {{
        position: absolute;
        padding-top: 10px;
        left: 70px;
        color: #ccc;
        font-size: 18px;
    }}

    .card-title-{unique_id} {{
        position: absolute;
        top: 100px;
        left: 20px;
        font-size: 32px;
        font-weight: bold;
        z-index: 3;
    }}

    .card-{unique_id} p {{
        position: absolute;
        top: 150px;
        left: 20px;
        width: 70%;
        padding: 10px 0;
        z-index: 3;
    }}
    </style>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <article class="card-{unique_id}">
            <div class="movie-bg-{unique_id}"></div>
            <figure class="chanel-logo-{unique_id}">
                <img src="{logo_url}" alt="Logo do Canal">
                <figcaption>
                    <h5>{formatted_caption}<br>{formatted_caption_hour}</h5>
                </figcaption>
            </figure>
            <h2 class="card-title-{unique_id}">{title}</h2>
            <p>{description}</p>
        </section>
    </article>
    """, unsafe_allow_html=True)
