# Streamlit Application with Folium Maps and Email Suggestion Feature

This Streamlit application combines interactive maps using both Folium and Situm, along with a feature for users to leave suggestions via email.

## Interactive Maps

The application offers two types of interactive maps:

1. **Map of Outside:** This map utilizes Folium to display outdoor locations within the Technical University of Lodz (TUL). It includes markers for various points of interest, such as the WEEIA faculty and the IFE faculty. Each marker provides additional information when clicked, enhancing the user experience.

2. **Inside Page with Embedded Situm Map:** This page features an embedded Situm map, showcasing indoor locations within specific buildings at TUL. Users can select a building from a dropdown menu, and the embedded map will display the corresponding indoor layout. To use the Situm map, you need to generate your own embed link on the Situm website and replace the `src` attribute of the embedded iframe with your generated link. This feature is particularly useful for navigating complex indoor environments.

### Usage

To access the interactive maps:

- Run the `main()` function in the provided Python script to view the Map of Outside.
- Navigate to the Inside Page with Embedded Situm Map to explore indoor locations.

## Email Suggestion Feature

In addition to the interactive maps, the application enables users to submit suggestions via email. Users can input their name and suggestion text, and upon submission, the suggestion will be sent to the specified recipient's email address.

### Usage

1. Enter your name and suggestion in the respective input fields.
2. Click the "Submit" button to send your suggestion.
3. A success message will be displayed upon successful submission.

## How to Run

To run the Streamlit application locally:

1. Ensure you have Python and Streamlit installed in your environment.
2. Clone this repository to your local machine.
3. Install the required dependencies using `pip install -r requirements.txt`.
4. Run the Streamlit application by executing `streamlit run app.py` in your terminal.

## Dependencies

- Streamlit: `streamlit`
- Folium: `folium`
- Streamlit Folium: `streamlit-folium`

## Configuration

Before running the application, make sure to configure the necessary API keys and secrets for services like Situm and email (if applicable). Additionally, generate your own Situm embed link on the Situm website to use the embedded Situm map feature.

## Note

For any issues or inquiries, feel free to open an issue in this repository.

Happy mapping and suggesting!
