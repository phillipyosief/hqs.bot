# ----------------------------------------------#
# hqs.bot ©                                     #
# by phillip.hqs ∫ Thanks to alphaSnosh         #
# ----------------------------------------------#

import botsetup
import logging


def discord_info():
    if botsetup.discord_info == True:
        logging.basicConfig(level=logging.INFO)
    if botsetup.discord_info == False:
        pass




