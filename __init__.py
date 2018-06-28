from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_handler


class WemoControllerUsingWitSkill(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_handler(IntentBuilder().require('WemoControllerUsingWit'))
    def handle_wemo_controller_using_wit(self, message):
        self.speak_dialog('wemo.controller.using.wit')


def create_skill():
    return WemoControllerUsingWitSkill()

