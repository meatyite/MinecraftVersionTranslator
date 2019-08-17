# MinecraftVersionTranslator
A python module used to create a translation of a minecraft version by creating your own string alteration function. <br/>
## Instructions & Examples
First, you'll need to go to your .minecraft folder (google it) and inside it click on the folder called `versions`.<br/>
Then you'll need to find the version you want to translate, <br/>and copy it's JAR to your project's folder and extract it using 7zip or winrar with the "extract to (folder name)" option. <br/>
Now here comes the fun part, translating minecraft.<br/>
Here's an example of a translator function, which will make every text in the game like the "uwu" meme.
```
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
    mc_translator.create_resource_pack()

```
Here are some ideas to what kind of translations you could do with this: <br/>
- Translating text to different languages and back using google translate's (or similar) API to make the text very broken
- Find a web tool that translates text into some form of dialect, reverse engineer it's API or scrape it then use in the translator (for example, what I did with [python-whoohoo](https://github.com/sl4vkek/python-whoohoo))
- Translate english into [Anglish](https://en.wikipedia.org/wiki/List_of_Germanic_and_Latinate_equivalents_in_English)
- You could do this with pretty much any language, I'm not restricting you to only english. There's lots of stuff you could do in various languages.
