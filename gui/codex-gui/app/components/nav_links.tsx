import Link from "next/link";

// links to display in the sidebar navigation
const links = [
    { name: "Home", href: "/" },
    { name: "Rulebook", href: "/rulebook" },
    { name: "Lorebook", href: "/lorebook" },
    { name: "Items", href: "/items" },
    { name: "Characters", href: "/characters" },
];

// TODO: import clsx, add it as styling for highlighted selection
export default function NavLinks() {
    return (
        <>
            {links.map(link => {
                return (
                    <Link key={link.name} href={link.name}>
                        <p className="hidden md:block">{link.name}</p>
                    </Link>
                )
            })}
        </>
    )
}