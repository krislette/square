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
      title: "Backend Developer",
      description: "Henry James Carlos",
      src: "acelle.jpg",
      ctaText: "Visit Github",
      ctaLink: "https://github.com/hjcarlos",
      content: (
        <p>
          Henry is responsible for the interface displaying
          generated lexemes in the terminal page  and worked
          on the syntax for operation symbols and for-loop            statements in the Square programming language.
        </p>
      ),
    },
    {
      title: "Frontend Developer",
      description: "Regina Bonifacio",
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
      title: "Backend Developer",
      description: "Fervicmar Lagman",
      src: "acelle.jpg",
      ctaText: "Visit Github",
      ctaLink: "https://github.com/perbik",
      content: (
        <p>
          Fervicmar contributes in the development, particularly in defining and implementing the tokenization process by identifying and categorizing tokens, ensuring accurate lexical analysis.
        </p>
      ),
    },
    {
      title: "Backend Developer",
      description: "Hans Christian Queja",
      src: "acelle.jpg",
      ctaText: "Visit Github",
      ctaLink: "https://github.com/HansQueja",
      content: (
        <p>
          Hans is one of the developers responsible in defining and implementing the tokenization process. He also contributes in identifying and categorizing tokens, standard processes in lexical analysis.
        </p>
      ),
    },
    {
      title: "Backend Developer",
      description: "Syruz Ken Domingo",
      src: "acelle.jpg",
      ctaText: "Visit Github",
      ctaLink: "https://github.com/sykeruzn",
      content: (
        <p>
          Syke is assigned to modify the changes in the programming language 
          documentation, proofread, and finalize the content in all sections.
          He also is a part of the backend development team.
        </p>
      ),
    },
    {
      title: "Frontend Developer",
      description: "Ylana Ong",
      src: "acelle.jpg",
      ctaText: "Visit Github",
      ctaLink: "https://github.com/jellyM0on",
      content: (
        <p>
          Ylana implemented the frontend editor component for code input and the file upload functionality. 
        </p>
      ),
    },
    {
      title: "Frontend Developer",
      description: "Duane Kyros Marzan",
      src: "acelle.jpg",
      ctaText: "Visit Github",
      ctaLink: "https://github.com/kyrariii",
      content: (
        <p>
          Kyros is in tasked with updating, reviewing, and polishing the programming language documentation.  He is also a member of the frontend development team.
        </p>
      ),
    },
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
