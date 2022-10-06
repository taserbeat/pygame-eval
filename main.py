from core.game import Game


def main():
    game = Game()

    try:
        game.run()
    except Exception:
        pass
    finally:
        game.quit()

    return


if __name__ == "__main__":
    main()
    exit(0)
