import os

import streamlit as st


def set_page():
    st.set_page_config(layout="wide")
    st.write("""
        ## Demo for Face-based voice conversion with F0 estimation
    """)


def get_data():
    path = "samples/deepfake"
    original_audio_names = os.listdir(path)

    data = []
    for fld in original_audio_names:
        file_names = os.listdir(os.path.join(path, fld))

        wav_filename = [name for name in file_names if name.endswith(".wav")][0]
        original_audio = os.path.join(path, fld, wav_filename)

        folders = [os.path.join(path, fld, name) for name in file_names if os.path.isdir(os.path.join(path, fld, name))]

        for fld_inside in folders:
            inside_data = os.listdir(fld_inside)
            image_name = [name for name in inside_data if (name.endswith(".jpeg") or name.endswith(".jpg"))][0]
            wav_name = [name for name in inside_data if name.endswith(".wav")][0]

            data.append({
                "original_audio": original_audio,
                "image": os.path.join(fld_inside, image_name),
                "synthesized_audio": os.path.join(fld_inside, wav_name)
            })

    return data


if __name__ == "__main__":
    set_page()
    rows_data = get_data()
    print(rows_data)

    st.title("Conversion samples")

    for i, row in enumerate(rows_data):
        st.markdown(f"### Sample {i + 1}")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("**Original Audio**")
            st.audio(row["original_audio"])
        
        with col2:
            st.markdown("**Reference Image**")
            st.image(row["image"], use_column_width=True)
        
        with col3:
            st.markdown("**Synthesized Audio**")
            st.audio(row["synthesized_audio"])
