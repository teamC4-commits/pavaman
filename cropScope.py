# import streamlit as st
# import numpy as np
# import tifffile as tiff
# import matplotlib.pyplot as plt
# import joblib
# import io
# from matplotlib import colormaps

# # Page setup
# st.set_page_config(page_title="Agri Analyzer", layout="wide")
# st.title("CropScope")
# st.markdown("Upload `.tiff` files for NDVI or NDRE-based crop analysis.")
# st.markdown("---")

# # Select Task
# mode = st.radio("Select Analysis Type", ["🌿 Health Classification (NDVI - 4 Bands)", "🌱 Growth Stage Estimation (NDRE - 8 Bands)"])

# # NDVI Mode
# if mode == "🌿 Health Classification (NDVI - 4 Bands)":
#     st.subheader("NDVI-Based Health Classification")
#     st.markdown("✅ Upload **4 single-band `.tiff` files**: Red, Green, NIR, Red Edge")

#     H_MS_R = st.file_uploader("Upload Red Band", type=["tif", "tiff"], key="ndvi_r")
#     H_MS_G = st.file_uploader("Upload Green Band", type=["tif", "tiff"], key="ndvi_g")
#     H_MS_NIR = st.file_uploader("Upload NIR Band", type=["tif", "tiff"], key="ndvi_nir")
#     H_MS_RE = st.file_uploader("Upload Red Edge Band", type=["tif", "tiff"], key="ndvi_re")

#     if all([H_MS_R, H_MS_G, H_MS_NIR, H_MS_RE]):
#         st.success("✅ All 4 NDVI bands uploaded successfully!")

#         red = tiff.imread(H_MS_R).astype(np.float32) / 65535.0
#         green = tiff.imread(H_MS_G).astype(np.float32) / 65535.0
#         nir = tiff.imread(H_MS_NIR).astype(np.float32) / 65535.0
#         re = tiff.imread(H_MS_RE).astype(np.float32) / 65535.0

#         # Calculate NDVI and NDRE
#         ndvi = (nir - red) / (nir + red + 1e-6)
#         ndre = (nir - re) / (nir + re + 1e-6)

#         # Normalize NDRE for color mapping
#         ndre_norm = (ndre - ndre.min()) / (ndre.max() - ndre.min())
#         green_rgb = np.stack([green]*3, axis=-1)
#         ndre_color = plt.get_cmap('RdYlGn')(ndre_norm)[..., :3]
#         overlay = (1 - 0.4) * green_rgb + 0.4 * ndre_color

#         # Display NDVI and NDRE overlay in same row
#         col1, col2 = st.columns(2)

#         with col1:
#             fig1, ax1 = plt.subplots(figsize=(6, 5))
#             im1 = ax1.imshow(ndvi, cmap='RdYlGn')
#             ax1.set_title("NDVI Map", fontsize=14)
#             ax1.axis('off')
#             fig1.colorbar(im1, ax=ax1, shrink=0.8)
#             st.pyplot(fig1, use_container_width=True)

#         with col2:
#             fig2, ax2 = plt.subplots(figsize=(6, 5))
#             ax2.imshow(overlay)
#             ax2.set_title("NDRE Nutrient Overlay", fontsize=14)
#             ax2.axis('off')
#             st.pyplot(fig2, use_container_width=True)

#         # --- Classification Result ---
#         try:
#             model = joblib.load("ndvi_model.pkl")
#             ndvi_flat = ndvi.flatten().reshape(1, -1)
#             predicted_label = model.predict(ndvi_flat)[0]
#             st.subheader("📊 Health Classification Result")
#             st.success(f"🧠 Predicted Vegetation Class: **{predicted_label}**")
#         except Exception as e:
#             st.error("🚫 Failed to load or run model.")
#             st.exception(e)

#         # --- NDRE Nutrient Interpretation ---
#         mean_ndre = ndre.mean()
#         st.markdown("### 📈 NDRE Nutrient Status")

#         if mean_ndre < 0.1:
#             st.error("❌ Deficient — Possible nitrogen stress or early growth stage.")
#         elif 0.1 <= mean_ndre <= 0.3:
#             st.success("✅ Optimal — Balanced nutrient condition.")
#         else:
#             st.warning("⚠️ Excessive — Possible over-fertilization or late growth stage.")

#     else:
#         st.warning("📂 Please upload all 4 required bands.")

# # NDRE Mode
# elif mode == "🌱 Growth Stage Estimation (NDRE - 8 Bands)":
#     st.subheader("NDRE-Based Growth Stage Estimation")

#     col1, col2 = st.columns(2)
#     with col1:
#         st.markdown("Timestamp for image 1 (Earlier)")
#         P1_MS_R = st.file_uploader("Upload Red Band", type=["tif", "tiff"], key="p1_r")
#         P1_MS_G = st.file_uploader("Upload Green Band", type=["tif", "tiff"], key="p1_g")
#         P1_MS_NIR = st.file_uploader("Upload NIR Band", type=["tif", "tiff"], key="p1_nir")
#         P1_MS_RE = st.file_uploader("Upload RE Band", type=["tif", "tiff"], key="p1_re")

#     with col2:
#         st.markdown("Timestamp Image2 (Later)")
#         P2_MS_R = st.file_uploader("Upload Red Band", type=["tif", "tiff"], key="p2_r")
#         P2_MS_G = st.file_uploader("Upload Green Band", type=["tif", "tiff"], key="p2_g")
#         P2_MS_NIR = st.file_uploader("Upload NIR Band", type=["tif", "tiff"], key="p2_nir")
#         P2_MS_RE = st.file_uploader("Upload RE Band", type=["tif", "tiff"], key="p2_re")

#     if all([P1_MS_R, P1_MS_G, P1_MS_NIR, P1_MS_RE, P2_MS_R, P2_MS_G, P2_MS_NIR, P2_MS_RE]):
#         st.success("✅ All 8 bands (Image 1 and Image 2) uploaded!")

#         def load_band(file): return tiff.imread(file).astype(np.float32) / 65535.0
#         p1_red, p1_green, p1_nir, p1_re = map(load_band, [P1_MS_R, P1_MS_G, P1_MS_NIR, P1_MS_RE])
#         p2_red, p2_green, p2_nir, p2_re = map(load_band, [P2_MS_R, P2_MS_G, P2_MS_NIR, P2_MS_RE])

#         def compute_index(numerator, denominator):
#             return (numerator - denominator) / (numerator + denominator + 1e-6)

#         ndvi_p1 = compute_index(p1_nir, p1_red)
#         ndre_p1 = compute_index(p1_nir, p1_re)
#         ndvi_p2 = compute_index(p2_nir, p2_red)
#         ndre_p2 = compute_index(p2_nir, p2_re)

#         # Row 1: P1 NDVI and NDRE
#         st.markdown("Timestamp for Image 1")
#         col_a, col_b = st.columns(2)
#         with col_a:
#             fig1, ax1 = plt.subplots()
#             ax1.imshow(ndvi_p1, cmap="RdYlGn")
#             ax1.axis("off")
#             st.pyplot(fig1, use_container_width=True)
#             st.caption("Image 1 - NDVI")
#         with col_b:
#             fig2, ax2 = plt.subplots()
#             ax2.imshow(ndre_p1, cmap="RdYlGn")
#             ax2.axis("off")
#             st.pyplot(fig2, use_container_width=True)
#             st.caption("Image1 - NDRE")

#         # Row 2: P2 NDVI and NDRE
#         st.markdown("Timestamp Image2")
#         col_c, col_d = st.columns(2)
#         with col_c:
#             fig3, ax3 = plt.subplots()
#             ax3.imshow(ndvi_p2, cmap="RdYlGn")
#             ax3.axis("off")
#             st.pyplot(fig3, use_container_width=True)
#             st.caption("Image2 - NDVI")
#         with col_d:
#             fig4, ax4 = plt.subplots()
#             ax4.imshow(ndre_p2, cmap="RdYlGn")
#             ax4.axis("off")
#             st.pyplot(fig4, use_container_width=True)
#             st.caption("image2 - NDRE")

#         # Row 3: NDRE Difference Map
#         st.markdown("### 🔁 NDRE Difference Map (Image2 - Image1)")
#         ndre_diff = ndre_p2 - ndre_p1
#         fig5, ax5 = plt.subplots(figsize=(8, 6))
#         im = ax5.imshow(ndre_diff, cmap="coolwarm", vmin=-0.3, vmax=0.3)
#         ax5.axis("off")
#         fig5.colorbar(im, ax=ax5, label="NDRE Δ")
#         st.pyplot(fig5, use_container_width=True)

#         # Growth Interpretation
#         mean_diff = float(np.nanmean(ndre_diff))
#         st.markdown(f"**Mean NDRE Change:** `{mean_diff:.4f}`")

#         if mean_diff > 0.05:
#             st.success("Crop growth observed — vegetation improved between timestamps.")
#         elif mean_diff < -0.05:
#             st.error("Crop regression or stress — vegetation declined.")
#         else:
#             st.warning("Minimal change detected — steady growth or stagnant.")

#     else:
#         st.warning("📂 Please upload all 8 bands (4 for Image1 + 4 for Image2).")
# # Footer
# st.markdown("---")
# st.caption("Developed by Team C4 - CropScope")





import streamlit as st
import numpy as np
import tifffile as tiff
import matplotlib.pyplot as plt
import joblib
import io
from matplotlib import colormaps

def app():  # ← wrapped the whole script
    # Page setup
    # st.set_page_config(page_title="Agri Analyzer", layout="wide")
    st.title("CropScope")
    st.markdown("Upload `.tiff` files for NDVI or NDRE-based crop analysis.")
    st.markdown("---")

    # Select Task
    mode = st.radio("Select Analysis Type", ["🌿 Health Classification (NDVI - 4 Bands)", "🌱 Growth Stage Estimation (NDRE - 8 Bands)"])

    # NDVI Mode
    if mode == "🌿 Health Classification (NDVI - 4 Bands)":
        st.subheader("NDVI-Based Health Classification")
        st.markdown("✅ Upload **4 single-band `.tiff` files**: Red, Green, NIR, Red Edge")

        H_MS_R = st.file_uploader("Upload Red Band", type=["tif", "tiff"], key="ndvi_r")
        H_MS_G = st.file_uploader("Upload Green Band", type=["tif", "tiff"], key="ndvi_g")
        H_MS_NIR = st.file_uploader("Upload NIR Band", type=["tif", "tiff"], key="ndvi_nir")
        H_MS_RE = st.file_uploader("Upload Red Edge Band", type=["tif", "tiff"], key="ndvi_re")

        if all([H_MS_R, H_MS_G, H_MS_NIR, H_MS_RE]):
            st.success("✅ All 4 NDVI bands uploaded successfully!")

            red = tiff.imread(H_MS_R).astype(np.float32) / 65535.0
            green = tiff.imread(H_MS_G).astype(np.float32) / 65535.0
            nir = tiff.imread(H_MS_NIR).astype(np.float32) / 65535.0
            re = tiff.imread(H_MS_RE).astype(np.float32) / 65535.0

            # Calculate NDVI and NDRE
            ndvi = (nir - red) / (nir + red + 1e-6)
            ndre = (nir - re) / (nir + re + 1e-6)

            # Normalize NDRE for color mapping
            ndre_norm = (ndre - ndre.min()) / (ndre.max() - ndre.min())
            green_rgb = np.stack([green]*3, axis=-1)
            ndre_color = plt.get_cmap('RdYlGn')(ndre_norm)[..., :3]
            overlay = (1 - 0.4) * green_rgb + 0.4 * ndre_color

            # Display NDVI and NDRE overlay in same row
            col1, col2 = st.columns(2)

            with col1:
                fig1, ax1 = plt.subplots(figsize=(6, 5))
                im1 = ax1.imshow(ndvi, cmap='RdYlGn')
                ax1.set_title("NDVI Map", fontsize=14)
                ax1.axis('off')
                fig1.colorbar(im1, ax=ax1, shrink=0.8)
                st.pyplot(fig1, use_container_width=True)

            with col2:
                fig2, ax2 = plt.subplots(figsize=(6, 5))
                ax2.imshow(overlay)
                ax2.set_title("NDRE Nutrient Overlay", fontsize=14)
                ax2.axis('off')
                st.pyplot(fig2, use_container_width=True)

            # --- Classification Result ---
            try:
                model = joblib.load("ndvi_model.pkl")
                ndvi_flat = ndvi.flatten().reshape(1, -1)
                predicted_label = model.predict(ndvi_flat)[0]
                st.subheader("📊 Health Classification Result")
                st.success(f"🧠 Predicted Vegetation Class: **{predicted_label}**")
            except Exception as e:
                st.error("🚫 Failed to load or run model.")
                st.exception(e)

            # --- NDRE Nutrient Interpretation ---
            mean_ndre = ndre.mean()
            st.markdown("### 📈 NDRE Nutrient Status")

            if mean_ndre < 0.1:
                st.error("❌ Deficient — Possible nitrogen stress or early growth stage.")
            elif 0.1 <= mean_ndre <= 0.3:
                st.success("✅ Optimal — Balanced nutrient condition.")
            else:
                st.warning("⚠️ Excessive — Possible over-fertilization or late growth stage.")

        else:
            st.warning("📂 Please upload all 4 required bands.")

    # NDRE Mode
    elif mode == "🌱 Growth Stage Estimation (NDRE - 8 Bands)":
        st.subheader("NDRE-Based Growth Stage Estimation")

        col1, col2 = st.columns(2)
        with col1:
            st.markdown("Timestamp for image 1 (Earlier)")
            P1_MS_R = st.file_uploader("Upload Red Band", type=["tif", "tiff"], key="p1_r")
            P1_MS_G = st.file_uploader("Upload Green Band", type=["tif", "tiff"], key="p1_g")
            P1_MS_NIR = st.file_uploader("Upload NIR Band", type=["tif", "tiff"], key="p1_nir")
            P1_MS_RE = st.file_uploader("Upload RE Band", type=["tif", "tiff"], key="p1_re")

        with col2:
            st.markdown("Timestamp Image2 (Later)")
            P2_MS_R = st.file_uploader("Upload Red Band", type=["tif", "tiff"], key="p2_r")
            P2_MS_G = st.file_uploader("Upload Green Band", type=["tif", "tiff"], key="p2_g")
            P2_MS_NIR = st.file_uploader("Upload NIR Band", type=["tif", "tiff"], key="p2_nir")
            P2_MS_RE = st.file_uploader("Upload RE Band", type=["tif", "tiff"], key="p2_re")

        if all([P1_MS_R, P1_MS_G, P1_MS_NIR, P1_MS_RE, P2_MS_R, P2_MS_G, P2_MS_NIR, P2_MS_RE]):
            st.success("✅ All 8 bands (Image 1 and Image 2) uploaded!")

            def load_band(file): return tiff.imread(file).astype(np.float32) / 65535.0
            p1_red, p1_green, p1_nir, p1_re = map(load_band, [P1_MS_R, P1_MS_G, P1_MS_NIR, P1_MS_RE])
            p2_red, p2_green, p2_nir, p2_re = map(load_band, [P2_MS_R, P2_MS_G, P2_MS_NIR, P2_MS_RE])

            def compute_index(numerator, denominator):
                return (numerator - denominator) / (numerator + denominator + 1e-6)

            ndvi_p1 = compute_index(p1_nir, p1_red)
            ndre_p1 = compute_index(p1_nir, p1_re)
            ndvi_p2 = compute_index(p2_nir, p2_red)
            ndre_p2 = compute_index(p2_nir, p2_re)

            # Row 1: P1 NDVI and NDRE
            st.markdown("Timestamp for Image 1")
            col_a, col_b = st.columns(2)
            with col_a:
                fig1, ax1 = plt.subplots()
                ax1.imshow(ndvi_p1, cmap="RdYlGn")
                ax1.axis("off")
                st.pyplot(fig1, use_container_width=True)
                st.caption("Image 1 - NDVI")
            with col_b:
                fig2, ax2 = plt.subplots()
                ax2.imshow(ndre_p1, cmap="RdYlGn")
                ax2.axis("off")
                st.pyplot(fig2, use_container_width=True)
                st.caption("Image1 - NDRE")

            # Row 2: P2 NDVI and NDRE
            st.markdown("Timestamp Image2")
            col_c, col_d = st.columns(2)
            with col_c:
                fig3, ax3 = plt.subplots()
                ax3.imshow(ndvi_p2, cmap="RdYlGn")
                ax3.axis("off")
                st.pyplot(fig3, use_container_width=True)
                st.caption("Image2 - NDVI")
            with col_d:
                fig4, ax4 = plt.subplots()
                ax4.imshow(ndre_p2, cmap="RdYlGn")
                ax4.axis("off")
                st.pyplot(fig4, use_container_width=True)
                st.caption("image2 - NDRE")

            # Row 3: NDRE Difference Map
            st.markdown("### 🔁 NDRE Difference Map (Image2 - Image1)")
            ndre_diff = ndre_p2 - ndre_p1
            fig5, ax5 = plt.subplots(figsize=(8, 6))
            im = ax5.imshow(ndre_diff, cmap="coolwarm", vmin=-0.3, vmax=0.3)
            ax5.axis("off")
            fig5.colorbar(im, ax=ax5, label="NDRE Δ")
            st.pyplot(fig5, use_container_width=True)

            # Growth Interpretation
            mean_diff = float(np.nanmean(ndre_diff))
            st.markdown(f"**Mean NDRE Change:** `{mean_diff:.4f}`")

            if mean_diff > 0.05:
                st.success("Crop growth observed — vegetation improved between timestamps.")
            elif mean_diff < -0.05:
                st.error("Crop regression or stress — vegetation declined.")
            else:
                st.warning("Minimal change detected — steady growth or stagnant.")

        else:
            st.warning("📂 Please upload all 8 bands (4 for Image1 + 4 for Image2).")
    # Footer
    st.markdown("---")
    st.caption("Developed by Team C4 - CropScope")

