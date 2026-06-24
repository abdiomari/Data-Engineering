from extract import extract
from transform import transform
from load import load

def main():
    raw_data = extract()
    transform_data = transform(raw_data)
    load(transform_data)
    print("Pipeline run is successful")

if __name__ == '__main__':
    main()