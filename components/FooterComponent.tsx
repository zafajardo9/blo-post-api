export default async function Footer() {
  return (
    <footer className="w-full border-t border-t-foreground/10 p-8 flex justify-center text-center text-xs">
      <p>
        Created by{" "}
        <a
          href="google.com"
          target="_blank"
          className="font-bold hover:underline"
          rel="noreferrer"
        >
          Zack
        </a>
      </p>
    </footer>
  );
}
