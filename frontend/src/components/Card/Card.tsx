import React, { useState } from "react";
import "./Card.css"; 

type Card = {
  title: string;
  description: string;
  src: string;
  ctaText: string;
  ctaLink: string;
  content: JSX.Element;
};

type ExpandableCardProps = {
  cards: Card[];
};

const ExpandableCard: React.FC<ExpandableCardProps> = ({ cards }) => {
  const [activeCard, setActiveCard] = useState<Card | null>(null);

  const handleCardClick = (card: Card) => {
    setActiveCard(card);
    document.body.style.overflow = card ? "hidden" : "auto";
  };

  const closeCard = () => {
    setActiveCard(null);
    document.body.style.overflow = "auto";
  };

  return (
    <div>
      {/* Overlay */}
      {activeCard && (
        <div className="overlay" onClick={closeCard}></div>
      )}

      {/* Expanded Card */}
      {activeCard && (
        <div className="expanded-card">
          <button className="close-btn" onClick={closeCard}>
            ×
          </button>
          <img src={activeCard.src} alt={activeCard.title} className="card-image" />
          <h3>{activeCard.title}</h3>
          <p>{activeCard.description}</p>
          <div className="card-content">{activeCard.content}</div>
          <a
            href={activeCard.ctaLink}
            target="_blank"
            rel="noopener noreferrer"
            className="cta-button"
          >
            {activeCard.ctaText}
          </a>
        </div>
      )}

      {/* Card Grid */}
      <div className="card-grid">
        {cards.map((card) => (
          <div
            key={card.title}
            className="card"
            onClick={() => handleCardClick(card)}
          >
            <img src={card.src} alt={card.title} className="card-image" />
            <h3>{card.title}</h3>
            <p>{card.description}</p>
          </div>
        ))}
      </div>
    </div>
  );
};

export default ExpandableCard;
