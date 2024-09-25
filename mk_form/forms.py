from django import forms
from django.core.exceptions import ValidationError

from mk_form.models import Data, Player, GameTypeCategory


# TODO: Use forms.Form instead, no 'fields = "__all__"'
class DataModelForm(forms.ModelForm):

    player_first = forms.ChoiceField()
    player_second = forms.ChoiceField()
    player_third = forms.ChoiceField()
    player_fourth = forms.ChoiceField()

    class Meta:
        model = Data
        fields = [
            "uid",
            "new_session",
            "session_uid",
            "game_type",
            "player_first",
            "player_second",
            "player_third",
            "player_fourth",
            "map_choice",
        ]

    def clean(self):
        cleaned_data = super().clean()
        player_first = cleaned_data.get("player_first")
        player_second = cleaned_data.get("player_second")
        player_third = cleaned_data.get("player_third")
        player_fourth = cleaned_data.get("player_fourth")

        game_type = cleaned_data.get("game_type")

        if (game_type == GameTypeCategory.TWO) & (player_first == player_second):
            msg = ValidationError(
                message=f"Game Type: {GameTypeCategory.TWO}, Player First can not be equal to Player Second."
            )

            self.add_error("game_type", msg)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        choices = Player.objects.values_list("name", flat=True)
        self.fields["player_first"].choices = [(name, name) for name in choices]
        self.fields["player_second"].choices = [(name, name) for name in choices]
        self.fields["player_third"].choices = [(name, name) for name in choices]
        self.fields["player_fourth"].choices = [(name, name) for name in choices]


class DataForm(forms.Form):
    pass
