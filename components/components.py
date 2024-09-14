import streamlit as st

def card_component(title, description, logo_url, logo_caption, background_image, unique_id):
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
        top: 150px;
        left: 20px;
        font-size: 32px;
        font-weight: bold;
        z-index: 3;
    }}

    .card-{unique_id} p {{
        position: absolute;
        top: 200px;
        left: 20px;
        width: 70%;
        padding: 10px 0;
        z-index: 3;
    }}
    </style>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <article class="card-{unique_id}">
        <section>
            <div class="movie-bg-{unique_id}"></div>
            <figure class="chanel-logo-{unique_id}">
                <img src="{logo_url}" alt="Logo do Canal">
                <figcaption>
                    <h5>{logo_caption}</h5>
                </figcaption>
            </figure>
            <h2 class="card-title-{unique_id}">{title}</h2>
            <p>{description}</p>
        </section>
    </article>
    """, unsafe_allow_html=True)
