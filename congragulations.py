def congratulations(name="kayleb"):
    message = f"Congratulations{' ' + name if name else ''}! 🎉"
    print(message)

if __name__ == "__main__":
    congratulations()
    congratulations("on your achievement")