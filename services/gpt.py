from openai import OpenAI
from conf.settings import GPT_API_KEY
from services.constants import INSTRUCTION, TEXT


class OpenAIClient:
    def __init__(self):
        self.client = OpenAI(api_key=GPT_API_KEY)

    def generate_answer(self, data: dict[str, list]) -> str | dict[str, str]:
        text = self.create_question(data)

        if not text:
            return {"error": "Текст для обработки не предоставлен"}

        try:
            response = self.client.chat.completions.create(
                model="gpt-4-turbo-preview",
                messages=[
                    {"role": "system", "content": INSTRUCTION},
                    {"role": "user", "content": text},
                ]
            )
            response_str = response.choices[0].message.content.strip()
            return response_str
        except Exception as e:
            return {"error": f"Ошибка при обработке текста: {e}"}

    @staticmethod
    def create_question(data: dict[str, list]) -> str | None:
        posts = data['3']
        if posts:
            result_posts = [f'{idx + 1}. {post}\n' for idx, post in enumerate(posts)]
            post_text = ''.join(result_posts)
            text = TEXT + post_text
            return text
        return None
