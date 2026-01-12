import argparse

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--a", type=int, required=True)
    p.add_argument("--b", type=int, required=True)
    p.add_argument("--op", choices=["add", "sub", "mul", "div"], default="add")
    args = p.parse_args()

    if args.op == "add":
        print(args.a + args.b)
    elif args.op == "sub":
        print(args.a - args.b)
    elif args.op == "mul":
        print(args.a * args.b)
    else:
        if args.b == 0:
            print("error: division by zero")
            return
        print(args.a / args.b)

if __name__ == "__main__":
    main()
