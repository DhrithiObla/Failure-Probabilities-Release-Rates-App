import streamlit as st
import pandas as pd

st. set_page_config(layout="wide")

tab1, tab2 = st.tabs(["Failure Rates", "Release Rates"])

with tab1:
    st.header("Failure Rates")

    st.subheader("Sources")

    col1, col2, col3, col4, col5, col6 = st.columns(6)

    with col1:
       st.markdown("[Fermilab ES&H, 4240TA-11-15](https://nasa.sharepoint.com/:b:/r/teams/IHTeam/Shared%20Documents/Cryogen%20Safety/Fermi%20Lab.pdf?csf=1&web=1&e=aimldu)") 

    with col2:
        st.markdown("[SLAC 2009, Pages 5-7 of 9](https://nasa.sharepoint.com/:b:/r/teams/IHTeam/Shared%20Documents/ODH%20and%20LEL%20Analysis/Failure%20%20Release%20Rates/SLAC%20Feb%202009.pdf?csf=1&web=1&e=BdjqiF)")
   
    with col3:
        st.markdown("[ESS-0038692, 14-16(17)](https://nasa.sharepoint.com/:b:/r/teams/IHTeam/Shared%20Documents/ODH%20and%20LEL%20Analysis/ESS-0038692.pdf?csf=1&web=1&e=uerZNT)")

    with col4:
        st.markdown("[S. Augustynowicz, 5](https://nasa.sharepoint.com/:b:/r/teams/IHTeam/Shared%20Documents/ODH%20and%20LEL%20Analysis/Oxygen%20Deficiency%20Hazard%20Analysis/Nicolleti%20Documents/ODH%20Paper.pdf?csf=1&web=1&e=tGYqeW)")

    with col5:
        st.markdown("[L. C. Cadwallader, 15](https://nasa.sharepoint.com/:b:/r/teams/IHTeam/Shared%20Documents/ODH%20and%20LEL%20Analysis/Failure%20%20Release%20Rates/SELECTED%20COMPONENT%20FAILURE%20RATE%20VALUES.pdf?csf=1&web=1&e=SOOeXC)")

    with col6:
        st.markdown("[Roymech, Pages 1-2 of 2](https://nasa.sharepoint.com/:b:/r/teams/IHTeam/Shared%20Documents/ODH%20and%20LEL%20Analysis/Failure%20Rates%20Roymech.co.uk.pdf?csf=1&web=1&e=6Ri7zP)")

    search_term = st.text_input("Search across all tables:")

    files = [
        "Bearings.csv", "Batteries.csv", "Circuit Breakers.csv", "Compressors.csv",
        "Dewars.csv", "Diesel.csv", "Electric Motors.csv", "Electrical Power.csv",
        "Fans.csv", "Filters.csv", "Flanges.csv", "Fuses.csv", "Gaskets.csv",
        "Gears.csv", "Header Piping.csv", "Instrumentation.csv", "Lines.csv",
        "Magnets.csv", "Motorized Louvers.csv", "Oil.csv", "Orifices.csv",
        "Piping.csv", "Pumps.csv", "Relays.csv", "Seals.csv", "Solid State Devices.csv",
        "Springs.csv", "Switches.csv", "Tank.csv", "Transformers.csv", "U tube.csv",
        "Valves.csv", "Vessels.csv", "Welds.csv", "Wires.csv", "Misc.csv"
    ]

    for file in files:
        df = pd.read_csv(file)
        df_display = df.copy()

        # Apply search filter if a term is provided
        if search_term:
            # Keep only rows where any cell contains the search term
            mask = df.apply(lambda row: row.astype(str).str.contains(search_term, case=False).any(), axis=1)
            df = df[mask]

            # Highlight search term in each cell
            def highlight(cell):
                cell_str = str(cell)
                return cell_str.replace(
                    search_term,
                    f"<mark style='background-color: red'>{search_term}</mark>"
                ) if search_term.lower() in cell_str.lower() else cell_str

            df = df.applymap(highlight)

        # Display only if there's data to show
        if not df.empty:
            st.markdown(f"### {file.replace('.csv', '')}")
            st.markdown(df.to_html(escape=False, index=False), unsafe_allow_html=True)


with tab2:

    st.header("Flow Rates")

    st.subheader("Sources")

    col1, col2, col3, col4, col5, col6, col7 = st.columns(7)

    with col1:
       st.markdown("[Kingston Model 115, Page 2](https://lqms.gsfc.nasa.gov/lqms-media/pvs/compfile/RV-Kingston-Model_115.pdf)") 

    with col2:
        st.markdown("[Kunkle Models 541, 542, & 548, Page 3](https://lqms.gsfc.nasa.gov/lqms-media/pvs/compfile/RV-Kunkle-542.pdf)")
   
    with col3:
        st.markdown("[Kingston Model 112, Page 2](https://lqms.gsfc.nasa.gov/lqms-media/pvs/compfile/RV-Kingston-112CSS.pdf)")

    with col4:
        st.markdown("[Kingston Model 119/118, Page 2](https://lqms.gsfc.nasa.gov/lqms-media/pvs/compfile/RV-Kingston-119CSS.pdf)")

    with col5:
        st.markdown("[Kingston Model KSV12 & KSV25, Page 2](https://lqms.gsfc.nasa.gov/lqms-media/pvs/compfile/RV-Kingston-KSV12__KSV25.pdf)")

    with col6:
        st.markdown("[Kunkle Models 6933, 6934, 6935, Page 5](https://lqms.gsfc.nasa.gov/lqms-media/pvs/compfile/RV-KUNKLE-Series_6000.pdf)")

    with col7:
        st.markdown("[NFPA 55 2005 Edition, 55-24](https://nasa.sharepoint.com/:b:/r/teams/IHTeam/Shared%20Documents/Standards,%20Program%20%26%20Policies/NFPA%2055.pdf?csf=1&web=1&e=TbcFqD)")

    st.subheader("Not a Relief Valve?")
    st.markdown("[Link to LQMS](https://lqms.gsfc.nasa.gov)")
    
    search_term = st.text_input("Search across all tables: ")

    files = [
        "Kingston Model 115.csv", "Kunkle Models 541, 542, & 548.csv", "Kingston Model 112.csv", "Kunkle Model 30.csv",
        "Kingston Model 119:118.csv", "Kingston Model KSV12 &KSV25.csv", "Kunkle Models 6933, 6934, 6935.csv", "NFPA 55 2005 Edition.csv"
    ]

    for file in files:
        df = pd.read_csv(file)
        df_display = df.copy()

        # Apply search filter if a term is provided
        if search_term:
            # Keep only rows where any cell contains the search term
            mask = df.apply(lambda row: row.astype(str).str.contains(search_term, case=False).any(), axis=1)
            df = df[mask]

            # Highlight search term in each cell
            def highlight(cell):
                cell_str = str(cell)
                return cell_str.replace(
                    search_term,
                    f"<mark style='background-color: red'>{search_term}</mark>"
                ) if search_term.lower() in cell_str.lower() else cell_str

            df = df.applymap(highlight)

        # Display only if there's data to show
        if not df.empty:
            st.markdown(f"### {file.replace('.csv', '')}")
            st.markdown(df.to_html(escape=False, index=False), unsafe_allow_html=True)
