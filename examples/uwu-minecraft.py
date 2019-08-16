from minecraftversiontranslator import MinecraftVersionTranslator


def uwuify_string(toUWU):
    return toUWU.lower().replace('r', 'w').replace('l', 'w').replace('n', 'ny')


if __name__ == '__main__':
    mc_translator = MinecraftVersionTranslator(
        extracted_version_folder_name='1.14.4',
        translate_function=uwuify_string,
        language_file_to_translate="en_us",
        new_language_file_name="en_uwu",
        language_name="uwu English",
        language_description="uwu English",
        language_region="US",
        language_bidirectional=False
    )
