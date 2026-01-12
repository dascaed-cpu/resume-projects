import argparse

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--a", type=int, required=True)
    p.add_argument("--b", type=int, required=True)
    print(args.a + args.b)

if __name__ == "__main__":
    main()
