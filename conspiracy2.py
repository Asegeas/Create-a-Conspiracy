from rich.console import Console
from rich.text import Text
from openai import OpenAI
console = Console()


def generate(name, styl, poliaff, belif) -> str:
    """Generate output of the prompt."""
    if len(belif) != 1:
        belif[-1] = f"and {belif[-1]}"
    option = 0 # edit for entered information
    prompts = [
        f"{styl}, make a conspiracy theory called {name}, that has {poliaff} affiliation and beliefs including: {belif}",           # Please make a function to tell if the belifs are larger than 1 and then put and at the end to make look good
        f"Make a funny conspiracy theory."
    ]
    client = OpenAI(
        # defaults to os.environ.get("OPENAI_API_KEY")

        api_key="",  # put your API_key here
    )

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "assistant",
                "content": f"You are a helpful internet user that generates conspiracy theories based on the following prompt: {prompts[option]}"
            }
        ],
        model="gpt-4",
    )
    return chat_completion


def poli_aff() -> None:
    """Displays the suggested options."""
    console.print("Political affiliation options:   ")
    console.print("1. far-right")
    console.print("2. right-wing")
    console.print("3. right-leaning")
    console.print("4. no-affiliation")
    console.print("5. left-leaning")
    console.print("6. left-wing")
    console.print("7. far-left")
    console.print("8. radical-right-wing")
    console.print("9. radical-left-wing")


def affiliation_fmt(poli_afl: str = "no political") -> str:
    """Correctly formats the user input."""
    if poli_afl == '1':
        poli_afl = 'far-right'
    if poli_afl == '2':
        poli_afl = 'right-wing'
    if poli_afl == '3':
        poli_afl = 'right-leaning'
    if poli_afl == '4':
        poli_afl = 'no political'
    if poli_afl == '5':
        poli_afl = 'left-leaning'
    if poli_afl == '6':
        poli_afl = 'left-wing'
    if poli_afl == '7':
        poli_afl = 'far-left'
    if poli_afl == '8':
        poli_afl = 'radical-right-wing'
    if poli_afl == '9':
        poli_afl = 'radical-left-wing'
    if poli_afl == 'no-affiliation':
        poli_afl = 'no political'
    return poli_afl


def writing_ops() -> None:
    """Displays stuff."""
    console.print("Style-options please enter (1,2...) or type In the style of....:   ")
    console.print("1. /pol 4-chan post")
    console.print("2. reddit post")
    console.print("3. news-article")
    console.print("4. Bar-bathroom-wall")  # need a new one
    console.print("5. empirical-research")  # see what this one does
    console.print("6. APA-style")  # test this one
    console.print("7. Wikipedia-edit (Citation needed)")  # what does this do
    console.print("8. /LGBT 4-chan post")
    console.print("9. Jaded-old-person")  # test this
    console.print("10. 4-year-old")  # test this
    console.print("11. gangster-rap")


def writing_style(wrt_stl: str = 'In the style of a news article'):
    """Converts the options."""
    if wrt_stl == '1':
        wrt_stl = 'In the style of a /pol 4-chan post'
    if wrt_stl == '2':
        wrt_stl = 'In the style of a reddit post'
    if wrt_stl == '3':
        wrt_stl = 'In the style of a news article'
    if wrt_stl == '4':
        wrt_stl = 'In the style of marker written on the wall of a bar bathroom'
    if wrt_stl == '5':
        wrt_stl = 'In the stle of empircical research'
    if wrt_stl == '6':
        wrt_stl = 'In APA style'
    if wrt_stl == '7':
        wrt_stl = "In the style of a unverified user of wikipedia's edit to a wikipedia page in need of a citation"
    if wrt_stl == '8':
        wrt_stl = 'In the style of a /LGBT 4-chan post'
    if wrt_stl == '9':
        wrt_stl = 'In the style of a jaded old person'
    if wrt_stl == '10':
        wrt_stl = "In the style of a 4 year old's first time trying to write english"
    if wrt_stl == '11':
        wrt_stl = "In the style of a gangster rap"
    return wrt_stl


def main():
    """Main function."""
    console.print("Welcome to Create-a-conspiracy!")
    name_of_c = input("     Please enter the name of the Consipracy theory you are trying to create:    ")

    console.print()
    poli_aff()

    political_affiliation = input(f"    Please enter the political affiliation of '{name_of_c}':    ")

    console.print()

    perspective = []
    writing_ops()
    styl = input("  Please enter your choice here:    ")
    styl = writing_style(styl)
    anotherone = True
    political_affiliation = affiliation_fmt(poli_afl=political_affiliation)
    while anotherone:
        perspective.append(input(f"  Please enter a single belief of {name_of_c} conspiracy:    "))
        choice = input("Would you like to add another belief y/n:    ")
        if choice == 'n':
            anotherone = False
    console.print(f"generating {name_of_c} as we speak please wait it may take several minutes....  ")
    refine_output = generate(name=name_of_c, styl=styl, poliaff=political_affiliation, belif=perspective)
    console.print(refine_output)
    # console.print(refine_output["choices"][0]["text"])


if __name__ == '__main__':
    main()

