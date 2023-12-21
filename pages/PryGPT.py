import streamlit as st
import pandas as pd

def main():
    st.markdown("<h3 style='text-align: center;'>Hasil Pengujian Generator and Discriminator Model Accuracy Data Dengan 1000 epochs</h3>", unsafe_allow_html=True)

    data = {
        'Literacy': ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'],
        'Epoch': [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],
        'D Loss': [0.996641, 1.077202, 1.516468, 0.466807, 0.828703, 0.407905, 0.669072, 0.657398, 0.546918, 0.691887],
        'Accuracy': [50.78, 56.25, 43.36, 78.52, 58.98, 79.69, 73.44, 76.17, 74.22, 72.27],
        'G Loss': [1.92073, 1.92444, 2.371171, 2.622881, 2.219804, 2.864509, 2.802930, 2.93177, 3.047591, 3.147644]
    }

    df = pd.DataFrame(data)

    # Set indeks dimulai dari 1
    df.set_index('Literacy', inplace=True)

    # Menampilkan tabel
    st.table(df)

   
    # Membuat dua baris dengan dua gambar di setiap baris
    st.markdown("<h3 style='text-align: center;'>Hasil Penelitian</h3>", unsafe_allow_html=True)
    st.markdown("", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        image_path1 = "images/data1.png"
        st.image(image_path1, caption=" Training Loss Generator dan Loss Discriminator", width=250, use_column_width=False)

        image_path2 = "images/data2a.png"
        st.image(image_path2, caption="Hasil Pemantauan dan Penerapan Model Diskriminator", width=250, use_column_width=False)

    with col2:
        image_path3 = "images/data2.png"
        st.image(image_path3, caption="Hasil Monitoring dan Implementasi Model Generator", width=340, use_column_width=False)

        image_path4 = "images/data2c.png"
        st.image(image_path4, caption="Hasil Pemantauan Model Gabungan Generator dan Diskriminator", width=320, use_column_width=False)

if __name__ == "__main__":
    main()
