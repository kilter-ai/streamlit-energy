# import streamlit as st
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns
# from io import BytesIO
#
# # App title
# st.title("📊 Data Analysis App for Excel/CSV Files")
#
# # Sidebar for file upload and options
# with st.sidebar:
#     st.header("Upload & Settings")
#     uploaded_file = st.file_uploader("Upload Excel or CSV file", type=["xlsx", "xls", "csv"])
#
#     if uploaded_file:
#         st.success("File uploaded successfully!")
#         file_details = {"FileName": uploaded_file.name, "FileType": uploaded_file.type}
#         st.write(file_details)
#
#     st.markdown("---")
#     st.markdown("### Analysis Options")
#     show_raw_data = st.checkbox("Show raw data", value=True)
#     analysis_type = st.selectbox("Select analysis type",
#                                  ["Quick Overview", "Statistical Summary", "Data Visualization", "Custom Analysis"])
#
# # Main content area
# if uploaded_file is not None:
#     # Read the file
#     try:
#         if uploaded_file.name.endswith('.csv'):
#             df = pd.read_csv(uploaded_file)
#         else:
#             df = pd.read_excel(uploaded_file)
#     except Exception as e:
#         st.error(f"Error reading file: {e}")
#         st.stop()
#
#     # Show raw data
#     if show_raw_data:
#         st.subheader("Raw Data")
#         st.dataframe(df)
#
#     # Quick Overview
#     if analysis_type == "Quick Overview":
#         st.subheader("Quick Data Overview")
#
#         col1, col2 = st.columns(2)
#         with col1:
#             st.metric("Number of Rows", df.shape[0])
#             st.metric("Number of Columns", df.shape[1])
#
#         with col2:
#             st.metric("Missing Values", df.isna().sum().sum())
#             st.metric("Duplicate Rows", df.duplicated().sum())
#
#         st.subheader("Data Types")
#         dtype_df = pd.DataFrame(df.dtypes, columns=["Data Type"])
#         st.dataframe(dtype_df)
#
#         st.subheader("Missing Values by Column")
#         missing_df = pd.DataFrame(df.isna().sum(), columns=["Missing Values"])
#         st.dataframe(missing_df[missing_df["Missing Values"] > 0])
#
#     # Statistical Summary
#     elif analysis_type == "Statistical Summary":
#         st.subheader("Statistical Summary")
#
#         st.write("Numerical Columns Summary")
#         st.dataframe(df.describe())
#
#         categorical_cols = df.select_dtypes(include=['object']).columns
#         if len(categorical_cols) > 0:
#             st.write("Categorical Columns Summary")
#             for col in categorical_cols:
#                 st.write(f"**{col}**")
#                 st.dataframe(df[col].value_counts())
#
#     # Data Visualization
#     elif analysis_type == "Data Visualization":
#         st.subheader("Data Visualization")
#
#         col1, col2 = st.columns(2)
#
#         with col1:
#             plot_type = st.selectbox("Select plot type",
#                                      ["Histogram", "Bar Plot", "Scatter Plot", "Box Plot", "Line Plot"])
#
#         with col2:
#             numerical_cols = df.select_dtypes(include=[np.number]).columns
#             categorical_cols = df.select_dtypes(include=['object']).columns
#
#             if plot_type in ["Histogram", "Box Plot"]:
#                 selected_col = st.selectbox("Select column", numerical_cols)
#             elif plot_type == "Bar Plot":
#                 selected_col = st.selectbox("Select column", categorical_cols)
#             elif plot_type == "Scatter Plot":
#                 x_col = st.selectbox("Select X axis", numerical_cols)
#                 y_col = st.selectbox("Select Y axis", numerical_cols)
#             elif plot_type == "Line Plot":
#                 x_col = st.selectbox("Select X axis", df.columns)
#                 y_col = st.selectbox("Select Y axis", numerical_cols)
#
#         # Generate the plot
#         fig, ax = plt.subplots()
#
#         if plot_type == "Histogram":
#             sns.histplot(df[selected_col], kde=True, ax=ax)
#             ax.set_title(f"Distribution of {selected_col}")
#         elif plot_type == "Bar Plot":
#             sns.countplot(data=df, y=selected_col, ax=ax, order=df[selected_col].value_counts().index)
#             ax.set_title(f"Count of {selected_col}")
#         elif plot_type == "Scatter Plot":
#             sns.scatterplot(data=df, x=x_col, y=y_col, ax=ax)
#             ax.set_title(f"{y_col} vs {x_col}")
#         elif plot_type == "Box Plot":
#             sns.boxplot(data=df, y=selected_col, ax=ax)
#             ax.set_title(f"Box Plot of {selected_col}")
#         elif plot_type == "Line Plot":
#             sns.lineplot(data=df, x=x_col, y=y_col, ax=ax)
#             ax.set_title(f"{y_col} over {x_col}")
#
#         st.pyplot(fig)
#
#         # Download plot option
#         buf = BytesIO()
#         fig.savefig(buf, format="png", dpi=300, bbox_inches="tight")
#         st.download_button("Download Plot", buf.getvalue(), "plot.png", "image/png")
#
#     # Custom Analysis
#     elif analysis_type == "Custom Analysis":
#         st.subheader("Custom Analysis")
#
#         st.write("Run your own pandas code on the dataframe (df)")
#         custom_code = st.text_area("Enter your pandas code", "df.head()")
#
#         try:
#             # This is potentially dangerous - in production, you'd want to sanitize inputs
#             exec(f"result = {custom_code}")
#             st.write(locals().get('result', 'No result returned'))
#         except Exception as e:
#             st.error(f"Error executing code: {e}")
#
#     # Export processed data
#     st.markdown("---")
#     st.subheader("Export Data")
#
#     output_format = st.selectbox("Select output format", ["CSV", "Excel"])
#     output_filename = st.text_input("Output filename (without extension)", "processed_data")
#
#     if st.button("Export Data"):
#         try:
#             if output_format == "CSV":
#                 csv = df.to_csv(index=False).encode('utf-8')
#                 st.download_button(
#                     "Download CSV",
#                     csv,
#                     f"{output_filename}.csv",
#                     "text/csv"
#                 )
#             else:
#                 output = BytesIO()
#                 with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
#                     df.to_excel(writer, index=False, sheet_name='Sheet1')
#                 st.download_button(
#                     "Download Excel",
#                     output.getvalue(),
#                     f"{output_filename}.xlsx",
#                     "application/vnd.ms-excel"
#                 )
#         except Exception as e:
#             st.error(f"Error exporting data: {e}")
#
# else:
#     st.info("👈 Please upload a file to get started")
#     st.markdown("""
#     ### Sample Data Analysis App Features:
#     - Upload Excel or CSV files
#     - View raw data
#     - Get quick overview (shape, missing values, data types)
#     - See statistical summaries
#     - Create visualizations (histograms, bar plots, scatter plots, etc.)
#     - Perform custom analysis with pandas
#     - Export processed data
#     """)

import os
from io import BytesIO

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import streamlit as st
from dotenv import load_dotenv

from auth import get_keycloak_login_url, get_token, get_user_info
from plots import daily_usage_bar_plot
# Load environment variables
load_dotenv()

# App title
st.title("📊 Multi-CSV Data Analysis App")

# Get URLs from environment variables
CSV_URLS = {
    "Usage": os.getenv("CSV_URL_1"),
    "Dataset 2": os.getenv("CSV_URL_2"),
    "Dataset 3": os.getenv("CSV_URL_3")
}

# Verify URLs are available
missing_urls = [name for name, url in CSV_URLS.items() if not url]
if missing_urls:
    st.error(f"Missing environment variables for: {', '.join(missing_urls)}")
    st.info("Please set CSV_URL_1, CSV_URL_2, and CSV_URL_3 in your .env file")
    st.stop()

# url2 = 'https://lemur-8.cloud-iam.com/auth/realms/bhoy-troy/protocol/openid-connect/auth'
# url1 = 'https://lemur-8.cloud-iam.com/'


# keycloak = login(
#     url="https://lemur-8.cloud-iam.com/",
#     realm="bhoy-troy",
#     client_id="local_streamlit",
# )
#
# keycloak2 = login(
#     url=url2,
#     realm="bhoy-troy",
#     client_id="local_streamlit",
# )

# keycloak = login(
#     url="http://localhost:8080",
#     realm="myrealm",
#     client_id="myclient",
#     custom_labels={
#         "labelButton": "Sign in",
#         "labelLogin": "Please sign in to your account.",
#         "errorNoPopup": "Unable to open the authentication popup. Allow popups and refresh the page to proceed.",
#         "errorPopupClosed": "Authentication popup was closed manually.",
#         "errorFatal": "Unable to connect to Keycloak using the current configuration."
#     }
# )
def main():
    # Sidebar controls
    with st.sidebar:
        st.header("Data Selection")
        selected_dataset = st.selectbox("Choose Dataset", list(CSV_URLS.keys()))

        st.markdown("---")
        st.header("Analysis Options")
        show_raw_data = st.checkbox("Show raw data", value=True)
        analysis_type = st.selectbox(
            "Analysis Type",
            ["Dataset Info", "Statistical Summary", "Data Visualization", "Compare Datasets"]
        )

    @st.cache_data(ttl=3600)  # Cache data for 1 hour
    def load_data(url):
        try:
            if url.startswith('http'):
                # Handle Google Docs URL (convert to direct download)
                if 'drive.google.com' in url:
                    file_id = url.split('/d/')[1].split('/')[0]
                    url = f'https://drive.google.com/uc?export=download&id={file_id}'
                return pd.read_csv(url)
            return pd.read_csv(url)
        except Exception as e:
            st.error(f"Error loading data: {e}")
            return None

    # Load all datasets
    datasets = {name: load_data(url) for name, url in CSV_URLS.items()}
    selected_df = datasets[selected_dataset]

    # Main display
    if selected_df is not None:
        if show_raw_data:
            st.subheader(f"Raw Data: {selected_dataset}")
            st.dataframe(selected_df.head(1000))

        if analysis_type == "Dataset Info":
            st.subheader("Dataset Information")

            col1, col2 = st.columns(2)
            with col1:
                st.metric("Rows", selected_df.shape[0])
                st.metric("Columns", selected_df.shape[1])

            with col2:
                st.metric("Missing Values", selected_df.isna().sum().sum())
                st.metric("Duplicate Rows", selected_df.duplicated().sum())

            st.subheader("Column Data Types")
            st.dataframe(pd.DataFrame(selected_df.dtypes, columns=["Data Type"]))

            st.subheader("Missing Values by Column")
            missing_df = pd.DataFrame(selected_df.isna().sum(), columns=["Missing Values"])
            st.dataframe(missing_df[missing_df["Missing Values"] > 0])

        elif analysis_type == "Statistical Summary":
            st.subheader("Statistical Summary")

            st.write("Numerical Columns:")
            st.dataframe(selected_df.describe())

            categorical_cols = selected_df.select_dtypes(include=['object', 'category']).columns
            if len(categorical_cols) > 0:
                st.write("Categorical Columns:")
                for col in categorical_cols:
                    st.write(f"**{col}**")
                    st.dataframe(selected_df[col].value_counts().head(20))

        elif analysis_type == "Data Visualization":
            st.subheader("Data Visualization")

            col1, col2 = st.columns(2)
            with col1:
                plot_type = st.selectbox(
                    "Plot Type",
                    ["Histogram", "Bar Chart", "Scatter Plot", "Box Plot", "Line Chart", 'Bar Plot']
                )

            with col2:
                numerical_cols = selected_df.select_dtypes(include=np.number).columns
                categorical_cols = selected_df.select_dtypes(include=['object', 'category']).columns

                if plot_type in ["Histogram", "Box Plot"]:
                    x_axis = st.selectbox("Select Column", numerical_cols)
                elif plot_type == "Bar Chart":
                    x_axis = st.selectbox("Select Column", categorical_cols)
                elif plot_type == "Bar Plot":
                    x_axis = st.selectbox("Select Column", categorical_cols)
                elif plot_type in ["Scatter Plot", "Line Chart"]:
                    x_axis = st.selectbox("X-Axis", selected_df.columns)
                    y_axis = st.selectbox("Y-Axis", numerical_cols)

            # Generate plot
            fig, ax = plt.subplots(figsize=(10, 6))

            if plot_type == "Histogram":
                sns.histplot(selected_df[x_axis], kde=True, ax=ax)
                ax.set_title(f"Distribution of {x_axis}")
            elif plot_type == "Bar Chart":
                sns.countplot(data=selected_df, y=x_axis, ax=ax,
                              order=selected_df[x_axis].value_counts().iloc[:20].index)
            # elif plot_type == "Bar Chart":
            #     sns.countplot(data=selected_df, y=x_axis, ax=ax,
            #                   order=selected_df[x_axis].value_counts().iloc[:20].index)
            elif plot_type == "Bar Plot":
                # sns.countplot(data=selected_df, y=x_axis, ax=ax,
                #           order=selected_df[x_axis].value_counts().iloc[:20].index)
                fig = daily_usage_bar_plot(selected_df)
                # ax.set_title(f"Count of {x_axis}")
            elif plot_type == "Scatter Plot":
                sns.scatterplot(data=selected_df, x=x_axis, y=y_axis, ax=ax)
                ax.set_title(f"{y_axis} vs {x_axis}")
            elif plot_type == "Box Plot":
                sns.boxplot(data=selected_df, y=x_axis, ax=ax)
                ax.set_title(f"Box Plot of {x_axis}")
            elif plot_type == "Line Chart":
                sns.lineplot(data=selected_df, x=x_axis, y=y_axis, ax=ax)
                ax.set_title(f"{y_axis} over {x_axis}")

            st.pyplot(fig)

            # Download option
            buf = BytesIO()
            fig.savefig(buf, format="png", dpi=300)
            st.download_button("Download Plot", buf.getvalue(), f"{plot_type}.png", "image/png")

        elif analysis_type == "Compare Datasets":
            st.subheader("Dataset Comparison")

            compare_col = st.selectbox(
                "Select column to compare",
                list(set.intersection(*(set(df.columns) for df in datasets.values())))
            )

            fig, ax = plt.subplots(figsize=(10, 6))
            for name, df in datasets.items():
                if compare_col in df.columns:
                    if df[compare_col].dtype in [np.number, 'float64', 'int64']:
                        sns.kdeplot(df[compare_col], label=name, ax=ax)
                    else:
                        sns.countplot(
                            y=df[compare_col].value_counts().iloc[:10].index,
                            data=df,
                            label=name,
                            ax=ax
                        )
            ax.set_title(f"Comparison of {compare_col} across datasets")
            ax.legend()
            st.pyplot(fig)

    # # Create a .env file if it doesn't exist
    # if not os.path.exists('.env'):
    #     with open('.env', 'w') as f:
    #         f.write("# Google Docs CSV URLs\n")
    #         f.write("CSV_URL_1=https://drive.google.com/...\n")
    #         f.write("CSV_URL_2=https://drive.google.com/...\n")
    #         f.write("CSV_URL_3=https://drive.google.com/...\n")
    #     st.sidebar.info("Created a template .env file. Please add your Google Docs URLs.")


def main2():
    st.title("Keycloak Authentication with Streamlit")

    # Check if user is authenticated
    if 'authenticated' not in st.session_state:
        print("Not authenticated")
        st.session_state.authenticated = False

    if not st.session_state.authenticated:
        # Handle OAuth callback
        query_params = st.query_params
        if 'code' in query_params:
            # import pdb;pdb.set_trace()

            try:
                code = query_params['code']
                tokens = get_token(code)
                user_info = get_user_info(tokens['access_token'])

                st.session_state.authenticated = True
                st.session_state.user_info = user_info
                st.session_state.tokens = tokens

                # Clear the code from URL
                # st.experimental_set_query_params()
                st.query_params.clear()

            except Exception as e:
                st.error(f"Authentication failed: {str(e)}")

        # Show login button
        st.markdown(f"[Login with Keycloak]({get_keycloak_login_url()})")

    else:
        print("Authenticated")
        # Display authenticated content
        user_info = st.session_state.user_info
        st.success(f"Welcome {user_info.get('name', user_info.get('preferred_username', 'User'))}!")

        # User info card
        with st.expander("User Information"):
            st.json(user_info)

        # Your main app content goes here
        st.write("This is your protected content")

        # Logout button
        if st.button("Logout"):
            st.session_state.authenticated = False
            st.session_state.clear()
            st.experimental_set_query_params()
            st.rerun()


if __name__ == "__main__":
    #     # if keycloak.authenticated:
    #     #     st.write(keycloak)
    #
    #
    #     st.title("Streamlit with Keycloak Authentication")
    #
    # # Check if the user is logged in
    # #     if not st.experimental_user.is_logged_in:
    #     st.write("You are not logged in.")
    #     if st.button("Log in with Keycloak"):
    #         st.login("keycloak")  # matches [auth.keycloak] in secrets.toml
    #     # else:
    #     #     # User is logged in
    #     #     st.write(f"Hello, {st.experimental_user.name}!")
    #     #     st.write("Email:", st.experimental_user.get("email", "N/A"))
    #     #     # ... any other user info from st.experimental_user
    #     #
    #     #     if st.button("Log out"):
    #     #         st.logout()
    #     main2()
    main()
