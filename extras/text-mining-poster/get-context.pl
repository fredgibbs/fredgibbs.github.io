#!/usr/bin/perl -w

my $string = quotemeta 'there';
my $slurp;
{
    local $/ = undef;
    open my $textfile, '<', './northanger.txt' or die $!;
    $slurp = <$textfile>;
    close $textfile;
}

while( $slurp =~ m/ ( .{0,25} $string.{0,25} )gisx / ) {
    print "Found $1\n";
}