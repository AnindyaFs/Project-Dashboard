import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Sample data, replace this with your actual data
hour_df = pd.read_csv('data/hour.csv')

# Streamlit app
st.set_page_config(page_title="Bike Rental Patterns")

st.title("Bike Rental Patterns")

# Create tabs for different pages
tab1, tab2 = st.tabs(["Based on Temperature", "Based on Hour"])

# selected_tab = st.radio("Select Page", ["Temperature Pattern", "Hourly Pattern"])
# Main content based on the selected tab
with tab1:
    # Header
    st.title("Based on Temperature")
    
    # Plot
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.lineplot(x="temp", y="cnt", data=hour_df, marker='o', color="Maroon", linewidth=2, ci=None, ax=ax)
    plt.title("Pola Jumlah Sewa Sepeda Berdasarkan Suhu")
    plt.xlabel("Suhu")
    plt.ylabel("Jumlah Sewa Sepeda")

    # Display the plot using Streamlit
    st.pyplot(fig)

    # Explanation
    st.write("""
    Rata-rata jumlah penyewaan sepeda memiliki peningkatan seiring meningkatnya suhu udara. 
    Jumlah penyewaan mencapai puncaknya pada saat suhu udara mencapai 48 derajat Celcius.
    """)

    st.write("""
    **- Minat tinggi ketika suhu naik :** Suhu udara yang lebih tinggi seringkali 
    membuat kondisi cuaca lebih menyenangkan. Pada suhu yang nyaman, orang lebih 
    cenderung ingin menghabiskan waktu di luar ruangan dan melakukan aktivitas fisik
    seperti bersepeda.""")

    st.write("""
    **- Aktivitas luar ruangan :** Musim panas cenderung menjadi waktu yang paling ideal 
    untuk beraktivitas di luar ruangan. Bersepeda tidak hanya merupakan olahraga yang baik 
    tetapi juga cara yang menyenangkan untuk menjelajahi lingkungan sekitar.""")

with tab2:
    # Header
    st.title("Based on Hour")

    # Selectbox to choose between "hr" and "workingday"
    attribute_option = st.radio("Select Attribute", ["Hour", "Working Day"])

    # Plot based on the selected attribute
    if attribute_option == "Hour":
        fig, ax = plt.subplots(figsize=(12, 6))
        colors = ["lightcoral"] * 24
        colors[17] = "maroon"  # Set color for the specified hour
        sns.barplot(x="hr", y="cnt", data=hour_df, ci=None, palette=colors, ax=ax)
        plt.title("Pola Jumlah Sewa Sepeda Berdasarkan Jam")
        plt.xlabel("Jam")
        plt.ylabel("Jumlah Sewa Sepeda")
        st.pyplot(fig)

        # Explanation for "hr"
        st.write("""
        Rata-rata penyewaan sepeda paling banyak terjadi pada jam 17 dan 18 atau jam 5 PM dan jam 6 PM dan juga pada pagi hari jam 8 AM. Paling sedikit penyewaan sepeda pada jam 4 AM.
        """)

        st.write("""
        **- Aktivitas rekreasi dan olahraga :** Banyak orang memilih bersepeda sebagai kegiatan rekreasi atau olahraga untuk memulai atau mengakhiri hari mereka. Pagi hari dapat menjadi waktu yang baik 
        untuk memulai hari dengan aktivitas yang menyegarkan, sementara sore hari memberikan kesempatan 
        untuk melepaskan stres setelah seharian bekerja.""")

        st.write("""
        **- Pola Transportasi Harian :** Jam 8 pagi adalah waktu yang umumnya sesuai dengan awal hari kerja, 
        dan banyak orang menggunakan sepeda sebagai sarana transportasi menuju tempat kerja atau sekolah 
        pada saat tersebut. Peningkatan penyewaan sepeda pada jam ini mencerminkan kebutuhan mobilitas pagi hari.
        Jam 5 atau jam 6 sore juga mencerminkan waktu pulang kerja atau sekolah, di mana banyak orang kembali ke rumah atau 
        melakukan kegiatan rekreasi. Penggunaan sepeda sebagai sarana pulang mungkin menjadi pilihan yang populer.""")

        st.write("""
        **- Pemandangan dan keamanan :** Pagi hari seringkali memberikan pemandangan yang indah dan keheningan di sekitar,
        membuat pengalaman bersepeda lebih menyenangkan. Sore hari juga menawarkan cahaya matahari yang lembut dan 
        kondisi cuaca yang bagus. Sebaliknya, pada malam hari, terutama setelah gelap, faktor keamanan dan pencahayaan 
        menjadi lebih berarti, dan beberapa orang mungkin merasa kurang nyaman untuk bersepeda pada waktu ini.""")
    
    elif attribute_option == "Working Day":
        # Plot based on "workingday"
        fig, ax = plt.subplots(figsize=(8, 5))
        sns.barplot(x="workingday", y="cnt", data=hour_df, ci=None, palette="viridis", ax=ax)
        plt.title("Pola Jumlah Sewa Sepeda pada Hari Kerja dan Hari Libur")
        plt.xlabel("Hari Kerja (1) / Hari Libur (0)")
        plt.ylabel("Jumlah Sewa Sepeda")
        st.pyplot(fig)
        # Explanation for "workingday"
        st.write("""
        Rata-rata penyewaan terjadi pada saat hari kerja (Senin - Jumat)
        """)

        st.write("""
        **- Transportasi menuju tempat kerja :** Banyak orang menggunakan sepeda sebagai sarana
        transportasi untuk pergi ke tempat kerja. Pilihan bersepeda dapat menjadi alternatif yang
        cepat, ekonomis, dan ramah lingkungan, terutama untuk perjalanan jarak pendek atau menengah. 
        Oleh karena itu, penyewaan sepeda lebih tinggi pada hari kerja karena banyak orang menggunakannya 
        sebagai sarana transportasi harian.
        """)

        st.write("""
        **- Kondisi lalu lintas :** Pada hari kerja, terutama selama jam sibuk, lalu lintas kendaraan bermotor 
        dapat menjadi masalah di beberapa kota. Bersepeda bisa menjadi pilihan yang lebih cepat dan praktis 
        dalam mengatasi kemacetan lalu lintas. Ini dapat meningkatkan minat penyewaan sepeda pada hari kerja 
        ketika orang lebih membutuhkan mobilitas yang efisien.
        """)
        st.write("""
        **- Jarak pendek dalam kota :** Pada hari kerja, banyak orang cenderung memiliki kegiatan di sekitar 
        area tempat tinggal atau tempat kerja mereka. Bersepeda dapat menjadi cara yang efisien untuk bergerak 
        di sekitar kota atau lingkungan tersebut, terutama jika jaraknya cukup dekat.
        """)

