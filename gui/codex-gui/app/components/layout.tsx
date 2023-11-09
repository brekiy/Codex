import Head from 'next/head';
import styles from './layout.module.css';

export const siteTitle = 'Cold Iron RPG Codex'

export default function Layout({ children }) {
    return (
        <div className={styles.container}>
            {children}
        </div>
    );
}