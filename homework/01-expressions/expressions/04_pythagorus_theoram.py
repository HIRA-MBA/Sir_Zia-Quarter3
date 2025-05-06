"""Pythagorus Theorem"""
import math

def main():
    base=float(input("Enter the length of base of triangle in cms == "))
    perpendicular=float(input("Enter the length of perpendicular of triangle in cms == "))
    hyp_square=(base*base)+(perpendicular*perpendicular)
    hyp=math.sqrt(hyp_square )
    print(f"\n The hypotenus {hyp_square } of triangle is {hyp} cms")


if __name__=="__main__":
    main()