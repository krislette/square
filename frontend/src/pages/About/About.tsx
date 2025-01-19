import './About.css';
import ExpandableCard from "../../components/Card/Card"

const cards = [
    {
      title: "Lead Developer",
      description: "Acelle Krislette Rosales",
      src: "acelle.jpg",
      ctaText: "Visit Github",
      ctaLink: "https://github.com/krislette",
      content: (
        <p>
          Oh loko anong balita ba't mainit
          Heto ako at sumesexy nag-iinit
          Umaapoy lumalagkit ang mga titig
          Hot mommy'ng malupit sumasarap 'pag may dumidilig
        </p>
      ),
    },
    {
      title: "Lead Developer",
      description: "Acelle Krislette Rosales",
      src: "acelle.jpg",
      ctaText: "Visit Github",
      ctaLink: "https://github.com/krislette",
      content: (
        <p>
          Oh loko anong balita ba't mainit
          Heto ako at sumesexy nag-iinit
          Umaapoy lumalagkit ang mga titig
          Hot mommy'ng malupit sumasarap 'pag may dumidilig
        </p>
      ),
    },
    {
      title: "Lead Developer",
      description: "Acelle Krislette Rosales",
      src: "acelle.jpg",
      ctaText: "Visit Github",
      ctaLink: "https://github.com/krislette",
      content: (
        <p>
          Oh loko anong balita ba't mainit
          Heto ako at sumesexy nag-iinit
          Umaapoy lumalagkit ang mga titig
          Hot mommy'ng malupit sumasarap 'pag may dumidilig
        </p>
      ),
    },
    {
      title: "Lead Developer",
      description: "Acelle Krislette Rosales",
      src: "acelle.jpg",
      ctaText: "Visit Github",
      ctaLink: "https://github.com/krislette",
      content: (
        <p>
          Oh loko anong balita ba't mainit
          Heto ako at sumesexy nag-iinit
          Umaapoy lumalagkit ang mga titig
          Hot mommy'ng malupit sumasarap 'pag may dumidilig
        </p>
      ),
    },
    {
      title: "Lead Developer",
      description: "Acelle Krislette Rosales",
      src: "acelle.jpg",
      ctaText: "Visit Github",
      ctaLink: "https://github.com/krislette",
      content: (
        <p>
          Oh loko anong balita ba't mainit
          Heto ako at sumesexy nag-iinit
          Umaapoy lumalagkit ang mga titig
          Hot mommy'ng malupit sumasarap 'pag may dumidilig
        </p>
      ),
    },
    {
      title: "Lead Developer",
      description: "Acelle Krislette Rosales",
      src: "acelle.jpg",
      ctaText: "Visit Github",
      ctaLink: "https://github.com/krislette",
      content: (
        <p>
          Oh loko anong balita ba't mainit
          Heto ako at sumesexy nag-iinit
          Umaapoy lumalagkit ang mga titig
          Hot mommy'ng malupit sumasarap 'pag may dumidilig
        </p>
      ),
    },
    {
      title: "Lead Developer",
      description: "Acelle Krislette Rosales",
      src: "acelle.jpg",
      ctaText: "Visit Github",
      ctaLink: "https://github.com/krislette",
      content: (
        <p>
          Oh loko anong balita ba't mainit
          Heto ako at sumesexy nag-iinit
          Umaapoy lumalagkit ang mga titig
          Hot mommy'ng malupit sumasarap 'pag may dumidilig
        </p>
      ),
    },
    {
      title: "Lead Developer",
      description: "Acelle Krislette Rosales",
      src: "acelle.jpg",
      ctaText: "Visit Github",
      ctaLink: "https://github.com/krislette",
      content: (
        <p>
          Oh loko anong balita ba't mainit
          Heto ako at sumesexy nag-iinit
          Umaapoy lumalagkit ang mga titig
          Hot mommy'ng malupit sumasarap 'pag may dumidilig
        </p>
      ),
    },
    // Add more card objects as needed
  ];

export default function About() {
    return (
        <div className="about-page">
            {/* Add the ExpandableCard here */}
            <div className="expandable__card-section">
                <h2>About Developers</h2>
                <ExpandableCard cards={cards} />
            </div>
        </div>
    );
}
