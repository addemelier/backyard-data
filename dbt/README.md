# dbt/

dbt project for transforming raw Seattle permit data into analytical models.

- **models/staging/** — light cleanup of raw source tables
- **models/intermediate/** — business logic and joins
- **models/marts/** — final tables consumed by the map UI and Streamlit app
- **tests/** — dbt data tests
- **macros/** — reusable SQL macros
