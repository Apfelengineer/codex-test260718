import argparse
from pathlib import Path

import cv2


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="入力画像にCannyエッジ検出を適用して保存します。"
    )
    parser.add_argument("input_image", type=Path, help="入力画像のパス")
    parser.add_argument("output_image", type=Path, help="出力画像のパス")
    parser.add_argument(
        "--low-threshold",
        type=int,
        default=100,
        help="低いしきい値（初期値: 100）",
    )
    parser.add_argument(
        "--high-threshold",
        type=int,
        default=200,
        help="高いしきい値（初期値: 200）",
    )
    return parser.parse_args()


def main():
    args = parse_arguments()

    if args.low_threshold < 0 or args.high_threshold < 0:
        raise SystemExit("しきい値には0以上の整数を指定してください。")
    if args.low_threshold >= args.high_threshold:
        raise SystemExit("低いしきい値は高いしきい値より小さくしてください。")

    image = cv2.imread(str(args.input_image), cv2.IMREAD_GRAYSCALE)
    if image is None:
        raise SystemExit(f"画像を読み込めませんでした: {args.input_image}")

    blurred_image = cv2.GaussianBlur(image, (5, 5), 0)
    edge_image = cv2.Canny(
        blurred_image,
        args.low_threshold,
        args.high_threshold,
        L2gradient=True,
    )

    args.output_image.parent.mkdir(parents=True, exist_ok=True)
    if not cv2.imwrite(str(args.output_image), edge_image):
        raise SystemExit(f"画像を保存できませんでした: {args.output_image}")

    print(f"Cannyエッジ画像を保存しました: {args.output_image}")


if __name__ == "__main__":
    main()
