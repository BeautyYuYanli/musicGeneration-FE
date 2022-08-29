# musicGeneration-FE

It is a frontend for [musicGeneration](https://github.com/liuyunhaozz/musicGeneration), based on [abc.js](https://github.com/paulrosen/abcjs).

## Usage

GET `https://music-generation-fe.vercel.app` with a parameter `?abc=<abc-sheet>`, where `<abc-sheet>` is a base64 encoded string of an [ABC music sheet](https://abcnotation.com/). For example:

[https://music-generation-fe.vercel.app/?abc=VDpMYXNzIE8nIERhbGxvZ2lsbAolIE5vdHRpbmdoYW0gTXVzaWMgRGF0YWJhc2UKUzpUcmFkLCBhcnIgUGhpbCBSb3dlCk06Ni84Cks6RAp8OmR8IkMiZWRlIEcyR3wiRiJBMkEgIkc3IkcyR3wiQyJlZGUgRzJHfCJHNyJBMkIgIkMiYzI6fApkfCJDImUyYyAiRyJkMkJ8IkMiYzJjICJHIkJBR3wiQyJlMmMgIkciZDJkfCJDImUyZiBnM3wKIkYiYTJmICJDImcyZXwiRzciZjJkICJDImUzfCJDImVkZSBHMkd8Ikc3IkEyQiAiQyJjMnx8](https://music-generation-fe.vercel.app/?abc=VDpMYXNzIE8nIERhbGxvZ2lsbAolIE5vdHRpbmdoYW0gTXVzaWMgRGF0YWJhc2UKUzpUcmFkLCBhcnIgUGhpbCBSb3dlCk06Ni84Cks6RAp8OmR8IkMiZWRlIEcyR3wiRiJBMkEgIkc3IkcyR3wiQyJlZGUgRzJHfCJHNyJBMkIgIkMiYzI6fApkfCJDImUyYyAiRyJkMkJ8IkMiYzJjICJHIkJBR3wiQyJlMmMgIkciZDJkfCJDImUyZiBnM3wKIkYiYTJmICJDImcyZXwiRzciZjJkICJDImUzfCJDImVkZSBHMkd8Ikc3IkEyQiAiQyJjMnx8)