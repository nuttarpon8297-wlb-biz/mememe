import tiktoken
def num_tokens_from_string(string: str) -> int:
  encoding = tiktoken.encoding_for_model("gpt-4o")
  num_tokens = len(encoding.encode(string))
  return num_tokens
print(num_tokens_from_string("สวัสดีประเทศไทย"))