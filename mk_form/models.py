from django.db import models
from datetime import datetime


class BoolCategory(models.TextChoices):
    YES = "Yes"
    NO = "No"


class GameTypeCategory(models.TextChoices):
    TWO = "2"
    THREE = "3"
    FOUR = "4"


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


class Player(models.Model):

    name = models.CharField(
        unique=True, default="None", max_length=20, blank=True, null=True
    )

    def __str__(self):
        return self.name


class Data(models.Model):

    uid = models.AutoField(
        verbose_name="UID", primary_key=True, default=1, auto_created=True, unique=True
    )

    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)

    new_session = models.CharField(
        verbose_name="New Session",
        max_length=3,
        choices=BoolCategory.choices,
        default=BoolCategory.NO,
    )

    session_uid = models.IntegerField(verbose_name="Session UID", default=1)

    game_type = models.CharField(
        verbose_name="Game Type",
        max_length=1,
        choices=GameTypeCategory.choices,
        default=GameTypeCategory.FOUR,
    )

    player_first = models.CharField(
        verbose_name="Player (1st)",
        max_length=20,
        blank=True,
        null=True,
    )

    player_second = models.CharField(
        verbose_name="Player (2nd)",
        max_length=20,
        blank=True,
        null=True,
    )

    player_third = models.CharField(
        verbose_name="Player (3rd)",
        max_length=20,
        blank=True,
        null=True,
    )

    player_fourth = models.CharField(
        verbose_name="Player (4th)",
        max_length=20,
        blank=True,
        null=True,
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
