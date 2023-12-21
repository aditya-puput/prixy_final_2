import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="About This App",
    page_icon="ℹ️", 
)

title_alignment="""
    <style>
    p, h3, h1, h5, h6 {
    text-align: center
    }
    div:has(> img){
        width: 100% !important  
    }
    img{
        align-self: center
    }
    </style>
    """
st.markdown(title_alignment, unsafe_allow_html=True)

st.write("# NASA Mars Colorized")

st.header("")

st.markdown(
    """
    This app is a simple web app that retrieve Mars rover photos from [NASA's API](https://api.nasa.gov/). Unfortunately most of the raw photos from NASA are grayscale (black and white). This app can turn grayscale photos from NASA's rover into beautifull colorized photos. This app is powered by Generative Adversarial Network (GAN) model called [Pix2pix](https://arxiv.org/abs/1611.07004) founded by Phillip Isola to magically turn black-and-white photos into wonderfull colorized photos. The model was trained using [this notebook](https://www.kaggle.com/code/varunnagpalspyz/pix2pix-is-all-you-need) by [VARUN NAGPAL SPYZ](https://www.kaggle.com/varunnagpalspyz). You can also download raw and processed images easily using this app. Explore and enjoy Mars photos with this app!🎉
"""
)

st.header("")
st.markdown(
    """
    ### Mars Exploration Program
    """
)

st.image(Image.open("images/rover.jpg"), width=600)

st.write("")

st.markdown(
    """
    Mars Exploration Program (MEP) is a long-term effort to explore the planet Mars, funded and led by NASA. Formed in 1993, MEP has made use of orbital spacecraft, landers, and Mars rovers to explore the possibilities of life on Mars, as well as the planet's climate and natural resources. The program is managed by NASA's Science Mission Directorate by Doug McCuistion of the Planetary Science Division. As a result of 40% cuts to NASA's budget for fiscal year 2013, the Mars Program Planning Group (MPPG) was formed to help reformulate the MEP, bringing together leaders of NASA's technology, science, human operations, and science missions.

    A Mars rover is a motor vehicle designed to travel on the surface of Mars. Rovers have several advantages over stationary landers: they examine more territory, they can be directed to interesting features, they can place themselves in sunny positions to weather winter months, and they can advance the knowledge of how to perform very remote robotic vehicle control. They serve a different purpose than orbital spacecraft like Mars Reconnaissance Orbiter. A more recent development is the Mars helicopter.
"""
)

st.header("")


# Define the images
image_paths = [
    "images/black.jpg",
    "images/mars.jpeg",
    "images/nasa_1.jpg",
    "images/nasa_2.jpeg",
    "images/nasa_3.webp",
    "images/nasa_4.jpg",
    "images/nasa_5.jpeg",
    "images/nasa_6.jpeg",
    "images/nasa_7.jpg",
    "images/nasa_8.jpg",
    "images/nasa_9.jpeg",
    "images/nasa_10.jpg",
]

# Create two columns with different widths
col1, col2 = st.columns(2)

# Display two images in the first row
with col1:
    st.image(Image.open(image_paths[0]), width=300)
with col2:
    st.image(Image.open(image_paths[1]), width=300)

# Display the rest of the images in subsequent rows
for i in range(2, len(image_paths), 2):
    # Create two columns for each row
    col1, col2 = st.columns(2)

    # Display images in each column
    with col1:
        st.image(Image.open(image_paths[i]), width=300)
    with col2:
        # Ensure the last image is displayed even if there's an odd number of images
        if i + 1 < len(image_paths):
            st.image(Image.open(image_paths[i + 1]), width=300)


st.header("")
st.header("")

st.write("##### Creator")
st.image(Image.open("images/apry.jpg"), width=300)
st.write("##### Apry Aditya Saputra")
st.write("Universitas Negeri Yogyakarta")

st.header("")
st.header("")

st.write("##### Credits")
st.write("Isola, P., Zhu, J.-Y., Zhou, T., & Efros, A. A. (2016). Image-to-Image Translation with Conditional Adversarial Networks (Version 3). arXiv. https://doi.org/10.48550/ARXIV.1611.07004")
