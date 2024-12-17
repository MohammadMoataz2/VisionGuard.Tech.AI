import reflex as rx

suggestions_dict  = {
    "apple": ["apple pie", "apple cider", "apple tree", "apple watch"],
    "banana": ["banana bread", "banana smoothie", "banana tree"],
    "cherry": ["cherry blossom", "cherry pie", "cherry tree"],
    "date": ["date palm", "date night", "dates nutrition"],
}

class SearchEnginePage(rx.State):

    search_bar_value : str = ""

    list_of_suggestions: list = []




    def search_input_value(self, value):
        self.search_bar_value = value

        print("Value", value)

        if value:

            self.list_of_suggestions = self.get_suggestions(self.search_bar_value)
        else:
            self.list_of_suggestions = []



    def get_suggestions(self,query):
        query = query.lower()
        results = []
        for word, suggestion_list in suggestions_dict.items():
            if word.startswith(query):
                results.extend(suggestion_list)
        return results








def search_engine_page() -> rx.Component:
    return rx.container(
        rx.vstack(
            rx.heading("🛡️ Vision Guard", font_size="70px"),
            justify="center",
            align_items="center",
            padding_top="20px",  # Adjust padding to position at top center
            min_height="15vh",   # Adjust height for top positioning
        ),
        rx.container(
            rx.container(
            rx.heading(" 🔍Vision Guard Search", font_size="40px"),
    justify = "center",
    align_items = "center",
                margin_bottom="20px",
            ),
            rx.input(
                rx.input.slot(
                    rx.icon(tag="search"),
                ),
                placeholder="Search here...",
                on_change= SearchEnginePage.search_input_value,
            ),
            rx.container(
                rx.vstack(


                    SearchEnginePage.list_of_suggestions




                )



            ),
            justify="center",
            align_items="center",
            padding_top="10px",
            margin_top="200px",



        ),
        align_items="center",
        spacing="5",
        justify="center",
        min_height="85vh",  # Adjust to center input in remaining screen height
    )