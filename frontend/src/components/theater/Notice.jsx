export default function Notice({ title, children }) {
  return (
    <section>
      <span>{title}</span>
      {children}
    </section>
  );
}
