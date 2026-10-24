async function checkLink(url) {
  const response = await fetch("/check", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ url: url })
  });

  return await response.json();
}
