import { Title } from "../../pages/Theater";

export default function Notice({ title, children }) {
  return (
    <section>
      <span>
        소극장 <Title>{title}</Title>의 공지사항
      </span>
      {children}
    </section>
  );
}
