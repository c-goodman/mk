from typing import Literal, Any

from django import forms
from django.core.exceptions import ValidationError
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Row, Column, HTML, Submit

# from crispy_bootstrap5.bootstrap5 import BS5Accordion

from mk_form.models import Data, Player, GameTypeCategory, CharacterCategory


# TODO: Use forms.Form instead, no 'fields = "__all__"'
class DataModelForm(forms.ModelForm):

    player_first = forms.ChoiceField(initial="None")
    player_second = forms.ChoiceField(initial="None")
    player_third = forms.ChoiceField(initial="None")
    player_fourth = forms.ChoiceField(initial="None")

    def clean(self):
        cleaned_data = super().clean()
        player_first = cleaned_data.get("player_first")
        player_second = cleaned_data.get("player_second")
        player_third = cleaned_data.get("player_third")
        player_fourth = cleaned_data.get("player_fourth")

        character_first = cleaned_data.get("character_first")
        character_second = cleaned_data.get("character_second")
        character_third = cleaned_data.get("character_third")
        character_fourth = cleaned_data.get("character_fourth")

        game_type = cleaned_data.get("game_type")

        def validate_game_fields(
            fields: list[str],
            condition: Any,
            game_type_variable: Any | None,
            game_type_value: str,
            message: str,
        ) -> None:

            game_condition = (game_type_variable == game_type_value) & condition

            if game_condition:
                msg = ValidationError(
                    message=f"Game Type: {game_type_value}, {message}"
                )

                for field in fields:
                    self.add_error(field, msg)

        # Two Player Games
        # PRIMARY FIELDS ARE NOT NULL
        # 2P: Player First or Second can not be "None"
        validate_game_fields(
            fields=["player_first"],
            condition=(player_first == "None"),
            game_type_variable=game_type,
            game_type_value=GameTypeCategory.TWO,
            message="Player First can not be 'None'.",
        )

        validate_game_fields(
            fields=["player_second"],
            condition=(player_second == "None"),
            game_type_variable=game_type,
            game_type_value=GameTypeCategory.TWO,
            message="Player Second can not be 'None'.",
        )

        # 2P: Character First and Second can not be 'None'
        validate_game_fields(
            fields=["character_first"],
            condition=(character_first is None),
            game_type_variable=game_type,
            game_type_value=GameTypeCategory.TWO,
            message="Character First can not be 'None'.",
        )

        validate_game_fields(
            fields=["character_second"],
            condition=(character_second is None),
            game_type_variable=game_type,
            game_type_value=GameTypeCategory.TWO,
            message="Character Second can not be 'None'.",
        )

        # NOT REQUIRED FIELDS ARE NULL
        # 2P: Player Third and Fourth must be 'None'
        validate_game_fields(
            fields=["player_third"],
            condition=(player_third != "None"),
            game_type_variable=game_type,
            game_type_value=GameTypeCategory.TWO,
            message="Player Third must be 'None'.",
        )

        validate_game_fields(
            fields=["player_fourth"],
            condition=(player_fourth != "None"),
            game_type_variable=game_type,
            game_type_value=GameTypeCategory.TWO,
            message="Player Fourth must be 'None'.",
        )

        # 2P: Character Third and Fourth must be 'None'
        validate_game_fields(
            fields=["character_third"],
            condition=(character_third is not None),
            game_type_variable=game_type,
            game_type_value=GameTypeCategory.TWO,
            message="Character Third must be 'None'.",
        )

        validate_game_fields(
            fields=["character_fourth"],
            condition=(character_fourth is not None),
            game_type_variable=game_type,
            game_type_value=GameTypeCategory.TWO,
            message="Character Fourth must be 'None'.",
        )

        # PRIMARY FIELDS ARE UNIQUE
        # 2P: Player First can not equal Player Second
        validate_game_fields(
            fields=["player_first", "player_second"],
            condition=(player_first == player_second),
            game_type_variable=game_type,
            game_type_value=GameTypeCategory.TWO,
            message="Player First can not be equal to Player Second.",
        )

        # 2P: Character First can not equal Character Second
        validate_game_fields(
            fields=["character_first", "character_second"],
            condition=(
                len(
                    list(
                        set(
                            [
                                player_first,
                                player_second,
                            ]
                        )
                    )
                )
                != 2
            ),
            game_type_variable=game_type,
            game_type_value=GameTypeCategory.TWO,
            message="Character First can not be equal to Character Second.",
        )

        # 3 Player Games
        # PRIMARY FIELDS ARE NOT NULL
        # 3P: Player First, Second or Third can not be "None"
        validate_game_fields(
            fields=["player_first"],
            condition=(player_first == "None"),
            game_type_variable=game_type,
            game_type_value=GameTypeCategory.THREE,
            message="Player First can not be 'None'.",
        )

        validate_game_fields(
            fields=["player_second"],
            condition=(player_second == "None"),
            game_type_variable=game_type,
            game_type_value=GameTypeCategory.THREE,
            message="Player Second can not be 'None'.",
        )

        validate_game_fields(
            fields=["player_third"],
            condition=(player_third == "None"),
            game_type_variable=game_type,
            game_type_value=GameTypeCategory.THREE,
            message="Player Third can not be 'None'.",
        )

        # 3P: Character First, Second or Third can not be "None"
        validate_game_fields(
            fields=["character_first"],
            condition=(character_first is None),
            game_type_variable=game_type,
            game_type_value=GameTypeCategory.THREE,
            message="Character First can not be 'None'.",
        )

        validate_game_fields(
            fields=["character_second"],
            condition=(character_second is None),
            game_type_variable=game_type,
            game_type_value=GameTypeCategory.THREE,
            message="Character Second can not be 'None'.",
        )

        validate_game_fields(
            fields=["character_third"],
            condition=(character_third is None),
            game_type_variable=game_type,
            game_type_value=GameTypeCategory.THREE,
            message="Character Third can not be 'None'.",
        )

        # NOT REQUIRED FIELDS ARE NULL
        # 3P: Player Fourth must be 'None'
        validate_game_fields(
            fields=["player_fourth"],
            condition=(player_fourth != "None"),
            game_type_variable=game_type,
            game_type_value=GameTypeCategory.THREE,
            message="Player Fourth must be 'None'.",
        )

        validate_game_fields(
            fields=["character_fourth"],
            condition=(character_fourth is not None),
            game_type_variable=game_type,
            game_type_value=GameTypeCategory.THREE,
            message="Character Fourth must be 'None'.",
        )

        # PRIMARY FIELDS ARE UNIQUE
        # 3P: Players must be unique
        validate_game_fields(
            fields=["player_first", "player_second", "player_third"],
            condition=(
                (player_first == player_second)
                | (player_second == player_third)
                | (player_third == player_first)
            ),
            game_type_variable=game_type,
            game_type_value=GameTypeCategory.THREE,
            message="Player First, Second, and Third must be unique.",
        )

        # 3P: Characters must be unique
        validate_game_fields(
            fields=["character_first", "character_second", "character_third"],
            condition=(
                len(
                    list(
                        set(
                            [
                                player_first,
                                player_second,
                                player_third,
                            ]
                        )
                    )
                )
                != 3
            ),
            game_type_variable=game_type,
            game_type_value=GameTypeCategory.THREE,
            message="Character First, Second, and Third must be unique.",
        )

        # 4 Player Games
        # PRIMARY FIELDS ARE NOT NULL
        # 4P: Player First, Second, Third or Fourth can not be "None"
        validate_game_fields(
            fields=["player_first"],
            condition=(player_first == "None"),
            game_type_variable=game_type,
            game_type_value=GameTypeCategory.FOUR,
            message="Player First can not be 'None'.",
        )

        validate_game_fields(
            fields=["player_second"],
            condition=(player_second == "None"),
            game_type_variable=game_type,
            game_type_value=GameTypeCategory.FOUR,
            message="Player Second can not be 'None'.",
        )

        validate_game_fields(
            fields=["player_third"],
            condition=(player_third == "None"),
            game_type_variable=game_type,
            game_type_value=GameTypeCategory.FOUR,
            message="Player Third can not be 'None'.",
        )

        validate_game_fields(
            fields=["player_fourth"],
            condition=(player_fourth == "None"),
            game_type_variable=game_type,
            game_type_value=GameTypeCategory.FOUR,
            message="Player Fourth can not be 'None'.",
        )

        # 4P: Characters First, Second, Third or Fourth can not be "None"
        validate_game_fields(
            fields=["character_first"],
            condition=(character_first is None),
            game_type_variable=game_type,
            game_type_value=GameTypeCategory.FOUR,
            message="Character First can not be 'None'.",
        )

        validate_game_fields(
            fields=["character_second"],
            condition=(character_second is None),
            game_type_variable=game_type,
            game_type_value=GameTypeCategory.FOUR,
            message="Character Second can not be 'None'.",
        )

        validate_game_fields(
            fields=["character_third"],
            condition=(character_third is None),
            game_type_variable=game_type,
            game_type_value=GameTypeCategory.FOUR,
            message="Character Third can not be 'None'.",
        )

        validate_game_fields(
            fields=["character_fourth"],
            condition=(character_fourth is None),
            game_type_variable=game_type,
            game_type_value=GameTypeCategory.FOUR,
            message="Character Fourth can not be 'None'.",
        )

        # PRIMARY FIELDS ARE UNIQUE
        # 4P: Players must be unique
        validate_game_fields(
            fields=[
                "player_first",
                "player_second",
                "player_third",
                "player_fourth",
            ],
            condition=(
                len(
                    list(
                        set(
                            [
                                player_first,
                                player_second,
                                player_third,
                                player_fourth,
                            ]
                        )
                    )
                )
                != 4
            ),
            game_type_variable=game_type,
            game_type_value=GameTypeCategory.FOUR,
            message="Player First, Second, Third and Fourth must be unique.",
        )

        # 4P: Characters must be unique
        validate_game_fields(
            fields=[
                "character_first",
                "character_second",
                "character_third",
                "character_fourth",
            ],
            condition=(
                len(
                    list(
                        set(
                            [
                                character_first,
                                character_second,
                                character_third,
                                character_fourth,
                            ]
                        )
                    )
                )
                != 4
            ),
            game_type_variable=game_type,
            game_type_value=GameTypeCategory.FOUR,
            message="Character First, Second, Third and Fourth must be unique.",
        )

    def __init__(self, *args, **kwargs):
        super(DataModelForm, self).__init__(*args, **kwargs)

        choices = Player.objects.values_list("name", flat=True)
        self.fields["player_first"].choices = [(name, name) for name in choices] + [
            ("", "")
        ]
        self.fields["player_second"].choices = [(name, name) for name in choices] + [
            ("", "")
        ]
        self.fields["player_third"].choices = [(name, name) for name in choices] + [
            ("", "")
        ]
        self.fields["player_fourth"].choices = [(name, name) for name in choices] + [
            ("", "")
        ]

        # Crispy Forms
        self.helper = FormHelper(self)
        self.helper.form_method = "post"
        self.helper.form_class = "form-horizontal"

        # Define Layout
        self.helper.layout = Layout(
            Div(
                HTML("<br>"),
                Div(
                    Row(HTML("<h4>General</h4>")),
                    Row(
                        Column("game_type", css_class="col me-auto"),
                        Column("map_choice", css_class="col me-auto"),
                        css_class="align-items-end justify-content-center",
                    ),
                    css_class="container",
                ),
                HTML("<br>"),
                Div(
                    Row(HTML("<h4>Players</h4>")),
                    Row(
                        Column("player_first", css_class="col me-auto"),
                        Column("player_second", css_class="col me-auto"),
                        Column("player_third", css_class="col me-auto"),
                        Column("player_fourth", css_class="col me-auto"),
                        css_class="align-items-end justify-content-center",
                    ),
                    css_class="container",
                ),
                HTML("<br>"),
                Div(
                    Row(HTML("<h4>Players</h4>")),
                    Row(
                        Column("character_first", css_class="col me-auto"),
                        Column("character_second", css_class="col me-auto"),
                        Column("character_third", css_class="col me-auto"),
                        Column("character_fourth", css_class="col me-auto"),
                        css_class="align-items-end justify-content-center",
                    ),
                    css_class="container",
                ),
                css_class="form-group",
            ),
            HTML("<br>"),
            Div(
                HTML(
                    "<a href='{% url 'data_list'%}' class='btn btn-secondary'>Cancel</a>"
                ),
                Submit("submit", "Submit", css_class="col"),
                css_class="align-items-end justify-content-start",
            ),
        )

    class Meta:
        model = Data
        fields = [
            "game_type",
            "map_choice",
            "player_first",
            "player_second",
            "player_third",
            "player_fourth",
            "character_first",
            "character_second",
            "character_third",
            "character_fourth",
        ]
