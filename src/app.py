from frontend import ExcelValidadorUI
from backend import process_excel

def main():
    ui = ExcelValidadorUI()
    ui.display_header()

    upload_file = ui.upload_file()

    if upload_file:
        result, error =  process_excel(upload_file)
        ui.display_results(result, error)



if __name__ == "__main__":
    main()




# import streamlit as st


# st.set_page_config(
#     page_title="Validador de schema excel"
# )

# # titulo do app
# st.title("Insira o seu excel para validação")


# arquivo = st.file_uploader("Carregue seu arquivo Excel aqui", type=["xlsx"])


# if arquivo is not None:
#     st.success("O schema do arquivo Excel está correto!!!")
