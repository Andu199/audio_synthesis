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
                "additional_info": f"Audio {fld}",
                "original_audio": original_audio,
                "image": os.path.join(fld_inside, image_name),
                "synthesized_audio": os.path.join(fld_inside, wav_name)
            })

    return data


if __name__ == "__main__":
    set_page()
    rows_data = []
    for i in range(5, 0, -1):
        rows_data.append(
            {
                "additional_info": f"Audio Avram Iancu",
                "original_audio": "samples/avram/avram.wav",
                "image": f"samples/avram/avram{i}/avram{i}.jpg",
                "synthesized_audio": f"samples/avram/avram{i}/synth_avram{i}.wav"
            },
        )
        rows_data.append(
            {
                "additional_info": f"Audio Avram Iancu",
                "original_audio": "samples/avram/avram.wav",
                # "image": f"samples/avram_face_crop/avram{i}/face_crop_avram{i}.jpg",
                "image": f"samples/avram/avram{i}/avram{i}.jpg",
                "synthesized_audio": f"samples/avram_face_crop/avram{i}/synth_face_crop_avram{i}.wav"
            },
        )
    rows_data.extend(get_data())

    st.title("Conversion samples")

    for i, row in enumerate(rows_data):
        additional_info = row['additional_info']
        st.markdown(f"### Sample {i + 1} ({additional_info})")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if i < 10:
                st.markdown("**Original Audio (synthetized with ElevenLabs from text)**")
            else:
                st.markdown("**Original Audio**")
            st.audio(row["original_audio"])
        
        with col2:
            st.markdown("**Reference Image**")
            st.image(row["image"], use_container_width=True)
        
        with col3:
            st.markdown("**Synthesized Audio**")
            st.audio(row["synthesized_audio"])
