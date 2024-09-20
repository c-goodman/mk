from django.db import models


class PlayerCategory(models.TextChoices):
    RANDY = "Randy"
    COOPER = "Cooper"


class GameTypeCategory(models.TextChoices):
    TWO = "2"
    THREE = "3"
    FOUR = "4"


class PlaceCategory(models.TextChoices):
    FIRST = "1"
    SECOND = "2"
    THIRD = "3"
    FOURTH = "4"


class MapCategory(models.TextChoices):
    BB = ("Banshee Boardwalk", "Banshee Boardwalk")
    BC = ("Bowser's Castle", "Bowser's Castle")
    CM = ("Choco Mountain", "Choco Mountain")
    DKJ = ("D.K.'s Jungle", "D.K.'s Jungle")
    FS = ("Frappe Snowland", "Frappe Snowland")
    KD = ("Kalimari Desert", "Kalimari Desert")
    KTB = ("Koopa Troopa Beach", "Koopa Troopa Beach")
    LR = ("Luigi Raceway", "Luigi Raceway")
    MR = ("Mario Raceway", "Mario Raceway")
    MMF = ("Moo Moo Farm", "Moo Moo Farm")
    RR = ("Royal Raceway", "Royal Raceway")
    SL = ("Sherbert Land", "Sherbert Land")
    TT = ("Toad's Turnpike", "Toad's Turnpike")
    WS = ("Wario Stadium", "Wario Stadium")
    YV = ("Yoshi Valley", "Yoshi Valley")


class Data(models.Model):

    uid = models.IntegerField(verbose_name="UID", primary_key=True, default=1)

    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)

    session_uid = models.IntegerField(verbose_name="Session UID", default=1)

    player = models.CharField(
        verbose_name="Player",
        max_length=40,
        choices=PlayerCategory.choices,
        default=PlayerCategory.RANDY,
    )

    game_type = models.CharField(
        verbose_name="Game Type",
        max_length=1,
        choices=GameTypeCategory.choices,
        default=GameTypeCategory.FOUR,
    )

    place = models.CharField(
        verbose_name="Place",
        max_length=1,
        choices=PlaceCategory.choices,
        default=PlaceCategory.FIRST,
    )

    map_choice = models.CharField(
        verbose_name="Map",
        max_length=20,
        choices=MapCategory.choices,
        default=MapCategory.BB,
    )

    season = models.SmallIntegerField(verbose_name="Season", default=0)

    def __str__(self):
        return f"UID: {self.uid}"
