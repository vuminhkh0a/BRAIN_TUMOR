import streamlit as st

def explain(case):
    if case == 'Glioma':
        st.markdown(
            """
            ### Glioma  
            A **glioma** is a type of tumor that originates in the glial cells, which support and protect neurons in the brain and spinal cord.  
            Gliomas are considered **primary brain tumors** because they start in the brain rather than spreading from elsewhere.  
            
            They account for **about 30% of all brain and central nervous system tumors** and roughly **80% of malignant brain tumors**.  

            Common subtypes include:  
            - **Astrocytoma**: develops from astrocytes, can range from slow-growing to highly aggressive.  
            - **Glioblastoma (GBM)**: the most aggressive form, with rapid growth and poor prognosis.  
            - **Oligodendroglioma**: arises from oligodendrocytes, generally slower growing but still malignant.  
            - **Ependymoma**: originates from ependymal cells lining the ventricles of the brain or spinal cord.  

            **Symptoms** depend on location and size, but often include seizures, headaches, memory issues, and neurological deficits.  
            **Treatment** usually involves surgery, radiation therapy, and chemotherapy, but prognosis varies by tumor type and grade.  
            """
        )
        st.link_button("Wikipedia - Glioma", "https://en.wikipedia.org/wiki/Glioma")
        st.link_button("NIH - Glioma", "https://www.cancer.gov/types/brain/patient/adult-brain-treatment-pdq#_222")
        st.link_button("Mayo Clinic - Glioma", "https://www.mayoclinic.org/diseases-conditions/glioma")

    elif case == 'Meningioma':
        st.markdown(
            """
            ### Meningioma  
            A **meningioma** is typically a **slow-growing tumor** that develops from the meninges, the protective membranes covering the brain and spinal cord.  
            They are the most common type of primary brain tumor, making up about **30% of all brain tumors in adults**.  

            **Characteristics**:  
            - Often **benign (non-cancerous)**, though some can be atypical or malignant.  
            - More common in **women** (about twice as frequent as in men).  
            - Onset usually in **middle-aged to older adults**.  

            **Symptoms** (when present) may include:  
            - Headaches, vision problems, seizures  
            - Weakness on one side of the body  
            - Memory difficulties or personality changes  

            **Risk factors**: prior radiation exposure, genetic conditions (e.g., neurofibromatosis type 2).  

            **Treatment**: surgical removal is often curative; if surgery isn’t possible, radiation therapy or radiosurgery may be considered.  
            Most cases grow slowly and require only observation if asymptomatic.  
            """
        )
        st.link_button("Wikipedia - Meningioma", "https://en.wikipedia.org/wiki/Meningioma")
        st.link_button("NIH - Meningioma", "https://www.cancer.gov/types/brain/patient/adult-brain-treatment-pdq#_12")
        st.link_button("Johns Hopkins - Meningioma", "https://www.hopkinsmedicine.org/health/conditions-and-diseases/meningioma")

    elif case == 'No tumor':
        st.markdown("✅ Your brain is healthy and does not contain any tumors.")

    else:
        st.markdown(
            """
            ### Pituitary Tumors  
            **Pituitary tumors** are abnormal growths that develop in the **pituitary gland**, a pea-sized organ located at the base of the brain.  
            The pituitary controls many vital body functions through hormone production.  

            **Types**:  
            - **Pituitary adenomas**: benign and the most common, often slow-growing.  
            - **Functional tumors**: produce excess hormones (e.g., prolactin, growth hormone, ACTH).  
            - **Nonfunctional tumors**: do not produce hormones but can cause pressure effects.  

            **Symptoms** depend on tumor size and hormone activity:  
            - Hormonal imbalances (e.g., Cushing’s disease, acromegaly, infertility).  
            - Headaches and vision problems due to pressure on nearby structures.  

            **Treatment options**:  
            - Surgery (often through the nose using transsphenoidal surgery).  
            - Medications to control hormone levels.  
            - Radiation therapy for residual or recurrent tumors.  

            Most pituitary tumors are **benign and manageable**, but they can significantly affect quality of life if untreated.  
            """
        )
        st.link_button("Wikipedia - Pituitary tumor", "https://en.wikipedia.org/wiki/Pituitary_tumor")
        st.link_button("NIH - Pituitary tumor", "https://www.cancer.gov/types/pituitary/patient/pituitary-treatment-pdq")
        st.link_button("Cleveland Clinic - Pituitary tumor", "https://my.clevelandclinic.org/health/diseases/17582-pituitary-tumors")

    return
