import streamlit as st

import streamlit as st

def explain(case):
    if case == 'Glioma':
        st.markdown(
            """
            **Glioma** is a type of primary tumor that starts in the glial cells of the brain or spinal cord.  
            They are malignant but some are extremely slow to develop. Gliomas comprise about 30% of all brain and central nervous system tumors and 80% of all malignant brain tumors.  

            🔗 [Read more on Wikipedia](https://en.wikipedia.org/wiki/Glioma)
            """
        )
        st.link_button("Wikipedia - Glioma", "https://en.wikipedia.org/wiki/Glioma")

    elif case == 'Meningioma':
        st.markdown(
            """
            **Meningioma** (meningeal tumor) is typically a slow-growing tumor that forms from the meninges, 
            the membranous layers surrounding the brain and spinal cord. Symptoms depend on the location and occur as a result of the tumor pressing on nearby tissue.  

            🔗 [Read more on Wikipedia](https://en.wikipedia.org/wiki/Meningioma)
            """
        )
        st.link_button("Wikipedia - Meningioma", "https://en.wikipedia.org/wiki/Meningioma")

    elif case == 'No tumor':
        st.markdown("✅ Your brain is healthy and does not contain any tumors")

    else:
        st.markdown(
            """
            **Pituitary tumors** are unusual growths that develop in the pituitary gland, 
            a small organ about the size of a pea located behind the nose at the base of the brain.  
            They are usually benign (pituitary adenomas) and can be treated with surgery, medication, or radiation therapy.  

            🔗 [Read more on Wikipedia](https://en.wikipedia.org/wiki/Pituitary_tumor)
            """
        )
        st.link_button("Wikipedia - Pituitary tumor", "https://en.wikipedia.org/wiki/Pituitary_tumor")

    return

