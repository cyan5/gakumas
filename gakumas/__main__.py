from .Story import Story

def main():

    story: Story = Story("Pro")
    story.execution()

    del story

if __name__ == "__main__":
    main()
